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

@app.route('/users/auth/google', methods = ["POST"])
def auth_google():

    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return Response(
        response=json.dumps({'url':authorization_url}),
        status=200,
        mimetype='application/json'
    )  

@app.route('/users/callback', methods = ["GET"])
def callback():
    data = callback_google()
    return redirect(f"http://localhost:8080/login?token={data['token']}&expiry={data['expiry']}&picture={data['user_image']}&user_name={data['user_name']}")