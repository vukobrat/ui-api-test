import requests

from config.config import ENDPOINT_LOGIN


def test_login_api(user):
    user_token = user['token']

    login_data = {
        "username": user['user']['username'],
        "password": user['user']['password']
    }
    response = requests.post(ENDPOINT_LOGIN, data=login_data)
    assert response.status_code == 200
    assert response.json()['token'] == user_token


def test_login_wrong_username_api(user):
    login_data = {
        "username": '!',
        "password": user['user']['password']
    }
    response = requests.post(ENDPOINT_LOGIN, data=login_data)
    assert response.status_code == 404
    assert response.json()['success'] == False


def test_login_no_username_api(user):
    login_data = {
        "username": '',
        "password": user['user']['password']
    }
    response = requests.post(ENDPOINT_LOGIN, data=login_data)
    assert response.status_code == 400
    assert response.json()['username'][0] == 'This field may not be blank.'


def test_login_wrong_password_api(user):
    login_data = {
        "username": user['user']['username'],
        "password": "wrongpass"
    }
    response = requests.post(ENDPOINT_LOGIN, data=login_data)
    assert response.status_code == 400
    assert response.json()['success'] == False


def test_login_no_password_api(user):
    login_data = {
        "username": user['user']['username'],
        "password": ''
    }
    response = requests.post(ENDPOINT_LOGIN, data=login_data)
    assert response.status_code == 400
    assert response.json()['password'][0] == 'This field may not be blank.'