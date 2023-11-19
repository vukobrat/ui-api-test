import pytest
import requests

from config.config import ENDPOINT_SIGNUP
from tests.api.common.helpers import new_user_payload


@pytest.mark.api
def test_signup_api():
    new_user = new_user_payload()

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 201
    assert response.json()['success'] == 'Thanks for signing up.'


@pytest.mark.api
def test_signup_wrong_email_api():
    new_user = new_user_payload()
    new_user['email'] = 'wrong@'

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['email'][0] == 'Enter a valid email address.'


@pytest.mark.api
def test_signup_no_email_api():
    new_user = new_user_payload()
    new_user['email'] = ''

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['email'][0] == 'This field may not be blank.'


@pytest.mark.api
def test_signup_wrong_password_api():
    new_user = new_user_payload()
    new_user['password'] = '123'

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['password'][0] == 'Password must contain at least eight characters, one letter and one number.'


@pytest.mark.api
def test_signup_no_password_api():
    new_user = new_user_payload()
    new_user['password'] = ''

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['password'][0] == 'This field may not be blank.'


@pytest.mark.api
def test_signup_no_firstname_api():
    new_user = new_user_payload()
    new_user['firstName'] = ''

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['firstName'][0] == 'This field may not be blank.'


@pytest.mark.api
def test_signup_no_lastname_api():
    new_user = new_user_payload()
    new_user['lastName'] = ''

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['lastName'][0] == 'This field may not be blank.'


@pytest.mark.api
def test_signup_wrong_username_api():
    new_user = new_user_payload()
    new_user['username'] = '!marko'

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['username'][0] == 'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'


@pytest.mark.api
def test_signup_no_username_api():
    new_user = new_user_payload()
    new_user['username'] = ''

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['username'][0] == 'This field may not be blank.'


@pytest.mark.api
def test_signup_wrong_date_api():
    new_user = new_user_payload()
    new_user['dateOfBirth'] = '27/27/1970'

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['dateOfBirth'][0] == 'Date has wrong format. Use one of these formats instead: DD/MM/YYYY.'


@pytest.mark.api
def test_signup_invalid_date_age_api():
    new_user = new_user_payload()
    new_user['dateOfBirth'] = '1/1/2010'

    response = requests.post(ENDPOINT_SIGNUP, data=new_user)
    assert response.status_code == 400
    assert response.json()['dateOfBirth'][0] == 'You need to be at least 18 old to signup.'





