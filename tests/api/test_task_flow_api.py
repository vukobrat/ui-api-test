from tests.api.common.api import signup_user, login_user
from tests.api.common.helpers import create_post, create_comment, get_comments


def test_task_flow():
    # Register user
    new_user = signup_user()
    # Login
    logged_in_user = login_user(new_user)
    token = logged_in_user['token']
    # Create a post
    new_post = create_post(token)
    post_id = new_post.json()['id']

    # Create two comments for given post
    comment_1 = create_comment(token, post_id)
    comment_2 = create_comment(token, post_id)

    # expected values
    comment_1_id = comment_1.json()['id']
    comment_1_text = comment_1.json()['text']
    comment_2_id = comment_2.json()['id']
    comment_2_text = comment_2.json()['text']

    # Read comments
    read_comments = get_comments(token, post_id)

    assert read_comments.status_code == 200
    assert read_comments.json()['count'] == 2

    assert read_comments.json()['results'][1]['text'] == comment_1_text
    assert read_comments.json()['results'][1]['id'] == comment_1_id

    assert read_comments.json()['results'][0]['text'] == comment_2_text
    assert read_comments.json()['results'][0]['id'] == comment_2_id


