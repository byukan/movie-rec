from flask import Flask, render_template
from mov_rec import app


@app.route("/search/")
def search():
    print("in search view function, from module search.py")
    return render_template ('search.html', movie=None)
