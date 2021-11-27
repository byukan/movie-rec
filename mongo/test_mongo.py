from pymongo import MongoClient


def test_mongo_connect():
    client = MongoClient("mongodb+srv://m001-student:3@r.vu0ut.mongodb.net/movie?retryWrites=true&w=majority")
    db = client['movie']
    requested_similar_movie_object = db.similar_movies.find_one(1)
    expected_similar_movie_object = {'_id': 1,
                                     'similarity_scores': '[(1, 0.9999998), (3, 0.80469614), (412, 0.8000324), (238, 0.7922034), (953, 0.7791466), (40, 0.7775347), (172, 0.7746029), (294, 0.77392906), (974, 0.7722475), (560, 0.76852435)]'}
    assert requested_similar_movie_object == expected_similar_movie_object

    request_movie_object = db.movies.find_one(2)
    expected_movie_object = {'_id': 2,
                             'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@.jpg',
                             'Series_Title': 'The Dark Knight',
                             'Released_Year': '2008',
                             'Certificate': 'UA',
                             'Runtime': '152 min',
                             'Genre': 'Action, Crime, Drama',
                             'IMDB_Rating': 9.0,
                             'Overview': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                             'Meta_score': 84.0,
                             'Director': 'Christopher Nolan',
                             'Star1': 'Christian Bale',
                             'Star2': 'Heath Ledger',
                             'Star3': 'Aaron Eckhart',
                             'Star4': 'Michael Caine',
                             'No_of_Votes': 2303232,
                             'Gross': '534,858,444',
                             'title_overview': 'The Dark Knight When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'}

    assert request_movie_object == expected_movie_object
