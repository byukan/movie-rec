import unittest
from sys import maxsize

from mov_rec.database import set_next_id  # generates a random movie ID
from mov_rec.database import find_movie, similar_movies, movie_info  # related to individual movie page
from mov_rec.database import search_movies, highest_rated_movies  # home/search-page related


# to check ranking / sorting of results
def is_descending_order(nums):
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            return False
    return True


class TestSetNextId(unittest.TestCase):
    def test_set_next_id(self):
        for _ in range(5):
            assert 0 <= set_next_id() <= 999


class TestFindMovie(unittest.TestCase):
    def test_empty_id(self):  # null ID (note: this is never actually an input)
        result = find_movie(None)
        assert result is None

    def test_valid_id(self):  # valid IDs are between 0 and 999 inclusive
        result = find_movie(150)
        assert result is not None
        assert 'Series_Title' in result
        assert result['Series_Title'] == "Pan's Labyrinth"

    def test_zero(self):  # lowest possible valid ID
        result = find_movie(0)
        assert result is not None
        assert 'Series_Title' in result
        assert result['Series_Title'] == "The Shawshank Redemption"

    def test_max_valid_id(self):  # highest possible valid ID
        result = find_movie(999)
        assert result is not None
        assert 'Series_Title' in result
        assert result['Series_Title'] == "The 39 Steps"

    def test_negative_one(self):  # boundary case: ID below valid range
        result = find_movie(-1)
        assert result is None

    def test_minimum_int(self):  # extreme case: ID below valid range
        id = -maxsize - 1
        result = find_movie(id)
        assert result is None

    def test_one_thousand(self):  # boundary case: ID above valid range
        result = find_movie(1000)
        assert result is None

    def test_maximum_int(self):  # extreme case: ID above valid range
        result = find_movie(maxsize)
        assert result is None


# if the input (movie_id) is valid, similar_movies should return
# a list of tuples of the form (id, score) ordered by similarity score descending, with
# the first tuple corresponding to the same movie (a movie is most similar to itself)
class TestSimilarMovies(unittest.TestCase):
    def test_empty_id(self):  # null ID (note: this is never actually an input)
        similar_movie_ids = similar_movies(None)
        assert similar_movie_ids is None

    def test_valid_id(self):  # valid IDs are between 0 and 999 inclusive
        result = similar_movies(66)
        assert result is not None
        assert type(result) is list
        assert len(result) == 10
        assert type(result[0]) is tuple
        movie_ids, scores = zip(*result)
        assert is_descending_order(scores)
        assert movie_ids[0] == 66
        assert 1 - scores[0] < 0.00001

    def test_zero(self):  # lowest possible valid ID
        result = similar_movies(0)
        assert result is not None
        assert type(result) is list
        assert len(result) == 10
        assert type(result[0]) is tuple
        movie_ids, scores = zip(*result)
        assert movie_ids[0] == 0
        assert 1 - scores[0] < 0.00001
        assert is_descending_order(scores)

    def test_max_valid_id(self):  # highest possible valid ID
        result = similar_movies(999)
        assert result is not None
        assert type(result) is list
        assert len(result) == 10
        assert type(result[0]) is tuple
        movie_ids, scores = zip(*result)
        assert movie_ids[0] == 999
        assert 1 - scores[0] < 0.00001
        assert is_descending_order(scores)

    def test_negative_one(self):  # boundary case: ID below valid range
        result = similar_movies(-1)
        assert result is None

    def test_minimum_int(self):  # extreme case: ID below valid range
        id = -maxsize - 1
        result = similar_movies(id)
        assert result is None

    def test_one_thousand(self):  # boundary case: ID above valid range
        result = similar_movies(1000)
        assert result is None

    def test_maximum_int(self):  # extreme case: ID above valid range
        result = similar_movies(maxsize)
        assert result is None


class TestMovieInfo(unittest.TestCase):
    def test_empty_id(self):  # null ID (note: this is never actually an input)
        result, next_id = movie_info(None)
        assert result is None
        assert 0 <= next_id <= 999

    def test_valid_id_not_main(self):  # not the main movie to display; should not add suggestions
        movie, next_id = movie_info(99)
        assert movie is not None
        assert 'Series_Title' in movie
        assert movie['Series_Title'] == "Good Will Hunting"
        assert 'Suggestions' not in movie
        assert 0 <= next_id <= 999

    def test_valid_id_as_main(self):  # main movie to display; result should include suggestions
        movie, next_id = movie_info(170, True)
        assert movie is not None
        assert 'Series_Title' in movie
        assert movie['Series_Title'] == "Tonari no Totoro"
        assert 'Suggestions' in movie
        suggestions = movie['Suggestions']
        assert len(suggestions) == 9
        first_suggestion = suggestions[0]
        assert '_id' in first_suggestion
        assert first_suggestion['_id'] == 741
        assert 'Series_Title' in first_suggestion
        assert first_suggestion['Series_Title'] == "Le Petit Prince"
        assert 0 <= next_id <= 999


# The search_movies function returns a list of movies where the search term(s) appear(s)
# in the title, overview, genre, or names of director or cast.
# There should be at most 9 movies in the list, ranked by relevance.
class TestSearchMovies(unittest.TestCase):
    def test_empty_search_term(self):  # empty string in search (note: this is never actually an input)
        result = search_movies('')
        assert len(result) == 0

    def test_garbage_search_term(self):  # user submits faulty input
        result = search_movies('8p9y2;ihl;/')
        assert len(result) == 0

    def test_single_word(self):  # single common word in search string
        result = search_movies('escape')
        assert len(result) == 9
        assert result[0]['Series_Title'] == 'Escape from Alcatraz'  # score is higher if word appears earlier in title
        assert result[1]['Series_Title'] == 'The Great Escape'
        relevance_scores = [movie['score'] for movie in result]
        assert is_descending_order(relevance_scores)

    def test_multi_word_search(self):  # search for multiple words (in combination or separately)
        result = search_movies('dark knight')
        assert len(result) == 9
        assert result[0]['Series_Title'] == 'The Dark Knight'
        assert result[1]['Series_Title'] == 'The Dark Knight Rises'
        third = result[2]['Series_Title']
        assert 'Dark Knight' not in third
        assert 'Dark' in third or 'Knight' in third
        relevance_scores = [movie['score'] for movie in result]
        assert is_descending_order(relevance_scores)

    def test_exact_phrase(self):  # search for a combination of words in a particular order
        result = search_movies('"dark knight"')
        assert len(result) == 2
        assert result[0]['score'] >= result[1]['score']
        assert result[0]['Series_Title'] == 'The Dark Knight'
        assert result[1]['Series_Title'] == 'The Dark Knight Rises'

    def test_term_exclusion(self):  # exclude a term from the search
        result = search_movies('dark -knight')
        assert len(result) == 9
        titles = [movie['Series_Title'] for movie in result]
        assert 'Knight' not in titles


# highest_rated_movies should return the 9 most popular movies ranked by IMDB rating
class TestHighestRatedMovies(unittest.TestCase):
    def test_highest_rated_movies(self):
        result = highest_rated_movies()
        assert result is not None
        assert len(result) == 9
        assert result[0]['Series_Title'] == 'The Shawshank Redemption'  # verify most popular of all time
        ratings = [movie['IMDB_Rating'] for movie in result]
        assert is_descending_order(ratings)


if __name__ == '__main__':
    unittest.main()
