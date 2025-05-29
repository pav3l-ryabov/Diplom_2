import pytest

from credentials_generator import register_new_user_and_return_email_password_name
from methods.user_methods import UserMethods


@pytest.fixture
def create_user_and_delete():
    user_methods = UserMethods()
    email, password, name, access_token = register_new_user_and_return_email_password_name()
    yield {
        "email": email,
        "password": password,
        "name": name,
        "access_token": access_token
    }

    user_methods.delete_user(access_token)
