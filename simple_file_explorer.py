from flask import Flask
from auth import requires_auth

app = Flask(__name__)


@app.route('/')
@requires_auth
def hello_world():
    return 'Hello, World!'
