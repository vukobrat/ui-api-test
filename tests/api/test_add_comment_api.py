import pytest
import requests

from config.config import ENDPOINT_COMMENT
from tests.api.common.helpers import new_comment_payload, create_post


@pytest.mark.api
def test_add_comment_api(user):
    token = user['token']
    new_post = create_post(token)
    post_id = new_post.json()['id']

    headers = {
        'Authorization': f'token {token}'
    }

    new_comment = new_comment_payload()
    comment_payload = {
        "text": new_comment,
        "post": post_id
    }

    response = requests.post(ENDPOINT_COMMENT, data=comment_payload, headers=headers)
    assert response.status_code == 201
    assert response.json()['text'] == new_comment


@pytest.mark.api
def test_add_comment_wrong_post_id_api(user):
    token = user['token']
    post_id = 10000

    headers = {
        'Authorization': f'token {token}'
    }

    new_comment = new_comment_payload()
    comment_payload = {
        "text": new_comment,
        "post": post_id
    }

    response = requests.post(ENDPOINT_COMMENT, data=comment_payload, headers=headers)
    assert response.status_code == 400
    assert response.json()['errors']['post'][0] == 'Invalid pk "10000" - object does not exist.'
