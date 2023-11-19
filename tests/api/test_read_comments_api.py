import pytest
import requests

from config.config import ENDPOINT_READ_COMMENTS
from tests.api.common.helpers import create_post, create_comment


@pytest.mark.api
def test_read_comments_api(user):
    token = user['token']
    new_post = create_post(token)
    post_id = new_post.json()['id']

    new_comment = create_comment(token, post_id)
    comment_id = new_comment.json()['id']
    comment_text = new_comment.json()['text']

    headers = {
        'Authorization': f'token {token}'
    }

    url_fix = ENDPOINT_READ_COMMENTS.replace('{id}', str(post_id))
    response = requests.get(url_fix, headers=headers)

    assert response.status_code == 200
    assert response.json()['results'][0]['text'] == comment_text
    assert response.json()['results'][0]['id'] == comment_id



