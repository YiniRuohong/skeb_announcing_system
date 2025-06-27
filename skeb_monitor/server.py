from flask import Flask, jsonify
from .client import SkebClient
from . import Config

app = Flask(__name__)
client = SkebClient(Config.SKB_COOKIE)

@app.route('/api/artists')
def artists():
    data = client.get_following()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
