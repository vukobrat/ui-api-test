import pytest
import requests

from config.config import ENDPOINT_POST
from tests.api.common.helpers import new_post_payload


@pytest.mark.api
def test_add_post_api(user):
    token = user['token']
    new_post = new_post_payload()

    headers = {
        'Authorization': f'token {token}'
    }

    post_payload = {
        "text": new_post
    }

    response = requests.post(ENDPOINT_POST, data=post_payload, headers=headers)
    assert response.status_code == 201
    assert response.json()['text'] == new_post


@pytest.mark.api
def test_add_post_wrong_auth_api(user):
    new_post = '<img src="http://malicious.com/csrf?token=attacker_token"/>'

    headers = {
        'Authorization': f'token wrong'
    }

    post_payload = {
        "text": new_post
    }

    response = requests.post(ENDPOINT_POST, data=post_payload, headers=headers)
    assert response.status_code == 401
    assert response.json()['detail'] == 'Invalid token.'
