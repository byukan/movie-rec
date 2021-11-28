import pickle as p

import h


def test_compute_similarity():
    # use movies dataset
    df = p.load(open('/Users/b/movie-rec/model/imdb_top_10.p', 'rb'))
    sentences = df['Overview']
    shawshank_similar_movies = [0, 1, 4, 3, 6, 7, 9, 2, 5, 8]
    assert shawshank_similar_movies == [x for x, y in h.compute_similarity(0, sentences)]


def test_calculate_sentence_embedding():
    text = "Hercules must go from zero to hero to save the universe from Hades."
    v = h.calculate_sentence_embedding(text)
    hercules_embedding = p.load(open('/Users/b/movie-rec/model/hercules_embedding.p', 'rb'))
    assert (v == hercules_embedding).all()
