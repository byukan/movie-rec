import unittest
from mock_request import MockRequest
# from mov_rec import view_function_response
from mov_rec.view_movie import view_movie_response


class TestViewMovie(unittest.TestCase):
    def test_get_request(self):
        request = MockRequest(method='GET', args={'id': '150'}, form={})
        view_response = view_movie_response(request)
        assert view_response.render_response
        assert 'view_movie.html' == view_response.render_template
        assert 'movie' in view_response.kwargs
        assert 'next_id' in view_response.kwargs

        movie = view_response.kwargs.get('movie')
        next_id = view_response.kwargs.get('next_id')
        assert 'Suggestions' in movie
        # check that the suggestions list is correct

        assert movie['Series_Title'] == "Pan's Labyrinth"
        assert 0 <= next_id <= 999


if __name__ == '__main__':
    unittest.main()
