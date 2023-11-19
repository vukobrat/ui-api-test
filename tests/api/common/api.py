import requests

from config.config import ENDPOINT_SIGNUP, ENDPOINT_LOGIN
from tests.api.common.helpers import new_user_payload


def signup_user():
    new_user = new_user_payload()

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 201
    assert response.json()['success'] == 'Thanks for signing up.'
    return new_user


def login_user(user):
    login_data = {
        "username": user["username"],
        "password": user["password"]
    }
    response = requests.post(ENDPOINT_LOGIN, data=login_data)
    assert response.status_code == 200
    return response.json()
