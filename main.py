import os
from flask import Flask 
from flask import Blueprint, request, json
from flask.wrappers import Response
from flask.globals import session
from utils import callback_google, flow
from flask import request, current_app
from werkzeug.utils import redirect
from waitress import serve
from config import app_config


app = Flask(__name__)

app.config.from_object(app_config[os.getenv("FLASK_ENV")])


if __name__ == "__main__":
    app.run()

@app.route('/', methods = ["GET"])
def hello():

    print("Hello World!")