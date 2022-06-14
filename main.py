import requests as r
from flask import Flask

app = Flask(__name__)

@app.route("/search/<text>")
def search_movie(text):
    
    response = r.get(f"https://www.omdbapi.com/?apikey=59d1b0d8&s={text}")
    return response.json()