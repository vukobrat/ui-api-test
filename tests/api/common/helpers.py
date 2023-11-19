import uuid

import requests
from faker import Faker

from config.config import ENDPOINT_POST, ENDPOINT_COMMENT, ENDPOINT_READ_COMMENTS

fake = Faker()


def create_post(token):
    new_post = new_post_payload()

    headers = {
        'Authorization': f'token {token}'
    }

    post_payload = {
        "text": new_post
    }

    response = requests.post(ENDPOINT_POST, data=post_payload, headers=headers)
    assert response.status_code == 201
    return response


def create_comment(token, post_id):
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
    return response


def get_comments(token, post_id):
    headers = {
        'Authorization': f'token {token}'
    }

    url_fix = ENDPOINT_READ_COMMENTS.replace('{id}', str(post_id))
    response = requests.get(url_fix, headers=headers)
    assert response.status_code == 200
    return response

def new_post_payload():
    return fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)


def new_comment_payload():
    return fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)


def new_user_payload():
    email = f'test_user_{uuid.uuid4().hex}@symphony.is'
    password = "validPassword1"
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = fake.user_name()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=101).strftime('%d/%m/%Y')
    return {
        "email": email,
        "password": password,
        "firstName": first_name,
        "lastName": last_name,
        "username": username,
        "dateOfBirth": date_of_birth
    }
