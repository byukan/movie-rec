import unittest
from mock_request import MockRequest
# from mov_rec import view_function_response
from mov_rec.home import search_response


class TestSearch(unittest.TestCase):
    def test_get_request(self):
        request = MockRequest(method='GET', args={}, form={})
        view_response = search_response(request)
        assert view_response.render_response
        assert 'home.html' == view_response.render_template
        assert 'movies' in view_response.kwargs
        movies = view_response.kwargs.get('movies')
        assert len(movies) == 9
        # check that correct list was provided?

    def test_post_request(self):
        request = MockRequest(method='POST', args={}, form={'search_term': 'Paris'})
        view_response = search_response(request)
        assert view_response.render_response
        assert 'home.html' == view_response.render_template
        assert 'movies' in view_response.kwargs
        movies = view_response.kwargs.get('movies')
        assert len(movies) == 6  # check
        # check that correct list was provided?


if __name__ == '__main__':
    unittest.main()
