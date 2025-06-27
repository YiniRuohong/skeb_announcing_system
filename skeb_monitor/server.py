import os
from flask import Flask, jsonify, send_from_directory
from .client import SkebClient
from . import Config

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app = Flask(__name__)
client = SkebClient(Config.SKB_COOKIE)


@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')


@app.route('/app.js')
def frontend_js():
    return send_from_directory(FRONTEND_DIR, 'app.js')


@app.route('/style.css')
def frontend_css():
    return send_from_directory(FRONTEND_DIR, 'style.css')

@app.route('/api/artists')
def artists():
    data = client.get_following()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
