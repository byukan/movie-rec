# from mov_rec import db

from unittest.mock import Mock, patch 
from mov_rec.database import movie_info,  _set_next_id


# 1. mock the database
# datetime = Mock()

# 2. Add a return value to the mock
# datetime.datetime.today.return_value = datetime.datetime(year=2019, month=1, day=1)

# 3. Call the function
# is_weekday()

# db = Mock()

# db.movies.find_one.return_value = {"next_id": None}




# @patch('mov_rec.database.find_one')

@patch('mov_rec.database.similar_movies')
@patch('mov_rec.database.find_movie')
def test_similar_ids_are_added(find_movie_mock, similar_movies_mock):
    suggestions = [(1, 0.9), (2, 0.5), (3, 0.2)]
    find_movie_mock.return_value = {"next_id": None}
    similar_movies_mock.return_value = suggestions

    result = movie_info(58340535, is_suggestion=False)
    assert result is not None
    assert "Suggestions" in result
     # verify that [1, 2, 3] are added to suggestions
    


def test_set_next_id():
    result = {"next_id": None}
    _set_next_id(result)
    assert "next_id" in result
    assert 0 <= result["next_id"] <= 999


test_similar_ids_are_added()