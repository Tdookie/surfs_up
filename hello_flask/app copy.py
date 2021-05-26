import flask
from flask import Flask
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

export FLASK_APP=app.py