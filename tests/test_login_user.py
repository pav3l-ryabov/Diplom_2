import allure

from data.data import RESPONSE_BODY_AUTH_USER_WITH_INVALID_CREDS
from methods.user_methods import UserMethods


class TestCreateUser:

    @allure.title('Тест авторизации юзера')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем авторизует его и проверяет, что тело'
                        'ответа и статус соответствуют ожидаемым')
    def test_auth_user(self, create_user_and_delete):
        email, password, name, _ = create_user_and_delete
        payload = {
            "email": email,
            "password": password
        }
        response, status = UserMethods.login_user(self, payload)
        assert status == 200, f'Ожидали 200, получили {status}'
        assert all([
            response.json().get("success") is True,
            response.json().get("user", {}).get("email") == email,
            response.json().get("user", {}).get("name") == name]), f'Ответ не соответствует ожидаемому: {response.json()}'

    @allure.title('Тест авторизации юзера c неправильным паролем')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем авторизует его c неправильным паролем'
                        'и проверяет что авторизация не была успешной')
    def test_auth_invalid_user(self, create_user_and_delete):
        email, password, name, _ = create_user_and_delete
        payload = {
            "email": email,
            "password": "wrong_password"
        }
        response, status = UserMethods.login_user(self, payload)
        assert status == 401, f'Ожидали 401, получили {status}'
        assert RESPONSE_BODY_AUTH_USER_WITH_INVALID_CREDS == response.json(), \
            f'Ответ не соответствует ожидаемому: {response.json()}'