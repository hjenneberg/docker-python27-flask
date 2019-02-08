from flask import Flask
from flask_cors import CORS

import os
import socket

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Flask auf Python 2.7"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
