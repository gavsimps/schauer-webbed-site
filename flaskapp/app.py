from flask import Flask, render_template
import spotipy as spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
