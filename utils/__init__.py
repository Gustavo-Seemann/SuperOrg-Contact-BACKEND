import requests
import os
from flask import request, current_app
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow



def callback_google():

    try: 
        flow.fetch_token(authorization_response = request.url)
        credentials = flow.credentials
        request_session = requests.session()
        token_google = auth.transport.requests.Request(session=request_session)
        user_google_dict = id_token.verify_oauth2_token(
            id_token = credentials.id_token,
            request=token_google,
            audience=os.getenv("GOOGLE_CLIENT_ID"),
            clock_skew_in_seconds=0
        )

        data_auth = {
            "user_name": "",
            "user_image": "",
            "token": "",
            "expiry": ""
        }

        data_auth['user_name'] = user_google_dict['name']
        data_auth['user_image'] = user_google_dict['picture']
        data_auth['token'] = credentials.token
        data_auth['expiry'] = credentials.expiry

        return data_auth
    except Exception as e:
        print(e)


flow = Flow.from_client_secrets_file(
    client_secrets_file="database/client_secrets.json",
    scopes=[
        "https://www.googleapis.com/auth/contacts.readonly",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid"
    ],
    redirect_uri = "https://super-orgcontact-369704.uc.r.appspot.com/users/callback"
)


mimetype = 'application/json'

def get_user_contacts(token):
    headers = {
        'Content-type': mimetype,
        'Accept': mimetype
    }
    headers['Authorization'] = f"Bearer {token}"
    url = 'https://people.googleapis.com/v1/people/me/connections?personFields=names,emailAddresses'

    response = requests.get(url, headers=headers)
    return response


def exist_key(request_json, list_keys):
    keys_not_have_in_request = []

    for key in list_keys:
        if key in request_json:
            continue
        else:
            keys_not_have_in_request.append(key)

    if len(keys_not_have_in_request) == 0:
        return request_json

    return {"error": f"Está faltando o item {keys_not_have_in_request}"}