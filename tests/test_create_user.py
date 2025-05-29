import allure
import pytest

from data.data import RESPONSE_BODY_EXIST_USER, RESPONSE_BODY_CREATE_USER_WITHOUT_FIELDS, DATA_TEST_REG_WITHOUT_FIELDS
from methods.user_methods import UserMethods


class TestCreateUser:

    @allure.title('Тест создания рандомного юзера')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем проверяет, что все полученные поля'
                        'из ответа сервера не пусты(т.е. юзер создался, затем фикстура после yeld удаляет юзера')
    def test_create_new_random_user(self, create_user_and_delete):
        email, password, name, access_token = create_user_and_delete
        assert all((email, password, name, access_token)), \
            'пользователь не создался, т.к. ни одно из полей email, password, name, access_token не может быть пустым'

    @allure.title('Тест создания уже существующего юзера')
    @allure.description('Тест создает юзера с валидными рандомными кредами, потом снова пытается создать юзера с теми'
                        'же самыми кредами, затем проверяет статус и тело ответа, затем фикстура после yeld удаляет юзера')
    def test_create_existing_user(self, create_user_and_delete):
        email, password, name, _ = create_user_and_delete
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response, status = UserMethods.create_user(self, payload)
        assert status == 403, f'Ожидали 403, получили {status}'
        assert RESPONSE_BODY_EXIST_USER == response.json(), f'Ответ не соответствует ожидаемому: {response.json()}'

    @allure.title('Тест создания юзера c пустыми полями')
    @allure.description('Тест создает юзера с пустыми полями, параметризация используется для того, чтобы покрыть проверками'
                        'все случаи, проверки оптимизированы с помощью техники попарного тестирования')
    @pytest.mark.parametrize("payload", DATA_TEST_REG_WITHOUT_FIELDS)
    def test_create_new_user_without_required_field(self, payload):
        body_payload = payload
        response, status = UserMethods.create_user(self, body_payload)
        assert status == 403, f'Ожидали 403, получили {status}'
        assert RESPONSE_BODY_CREATE_USER_WITHOUT_FIELDS == response.json(), \
            f'Ответ не соответствует ожидаемому: {response.json()}'