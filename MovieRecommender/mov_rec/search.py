from flask import Flask, render_template
from mov_rec import app


@app.route("/search/")
def search():
    movies = [
        {
            '_id': 502,
            'Series_Title': "Iron Man",
            'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@.jpg'
        },
        {
            '_id': 103,
            'Series_Title': "Reservoir Dogs",
            'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@.jpg'
        },
        {
            '_id': 900,
            'Series_Title': "The Raid",
            'Poster_Link': 'https://m.media-amazon.com/images/M/MV5BZGIxODNjM2YtZjA5Mi00MjA5LTk2YjItODE0OWI5NThjNTBmXkEyXkFqcGdeQXVyNzQ1ODk3MTQ@.jpg'
        }
    ]

    print("in search view function, from module search.py")
    return render_template('search.html', movies=movies)
