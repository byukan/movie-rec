import unittest
from sys import maxsize

from mov_rec.database import _set_next_id, find_movie, movie_info, similar_movies, search_movies, highest_rated_movies


class TestSetNextId(unittest.TestCase):
    def test_set_next_id(self):
        assert 0 <= _set_next_id() <= 999


class TestFindMovie(unittest.TestCase):
    def test_empty_id(self):  # note: this is never actually an input
        result = find_movie(None)
        assert result is None

    def test_valid_id(self):  # id between 0 and 999 inclusive
        result = find_movie(150)
        assert result is not None
        assert "Series_Title" in result
        assert result["Series_Title"] == "Pan's Labyrinth"

    def test_zero(self):
        result = find_movie(0)
        assert result is not None
        assert "Series_Title" in result
        assert result["Series_Title"] == "The Shawshank Redemption"

    def test_max_valid_id(self):
        result = find_movie(999)
        assert result is not None
        assert "Series_Title" in result
        assert result["Series_Title"] == "The 39 Steps"

    def test_negative_one(self):
        result = find_movie(-1)
        assert result is None

    def test_minimum_int(self):
        id = -maxsize - 1
        result = find_movie(id)
        assert result is None

    def test_one_thousand(self):
        result = find_movie(1000)
        assert result is None

    def test_maximum_int(self):
        result = find_movie(maxsize)
        assert result is None


if __name__ == '__main__':
    unittest.main()
