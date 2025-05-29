import allure
import pytest

from data.data import RESPONSE_BODY_EXIST_USER, RESPONSE_BODY_CREATE_USER_WITHOUT_FIELDS, DATA_TEST_REG_WITHOUT_FIELDS, \
    VALID_ORDER, INVALID_ORDER, EMPTY_ORDER
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:

    @allure.title('Тест создания заказа с ингредиентом с авторизацией')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем создает заказ для этого юзера и проверяет,'
                        'что сервер ответил корректно')
    def test_create_new_order_with_auth(self, create_user_and_delete):
        _, _, _, access_token = create_user_and_delete
        payload = VALID_ORDER
        response, status = OrderMethods.create_order(self, payload, access_token)
        assert status == 200, f'Ожидали 200, а получили {status}'
        assert response.json().get("success") is True, f'Ожидали success: true, получили {response}'

    @allure.title('Тест создания заказа с ингредиентом без авторизации')
    @allure.description('Тест создает заказ с неправильным токеном и проверяет, что сервер ответил корректно')
    #убрал фикстуру create_user_and_delete, т.к. в этом тесте в ней нет смысла, мы ничего не передаем, кроме
    #заведомо неправильного токена
    def test_create_new_order_without_auth(self):
        payload = VALID_ORDER
        response, status = OrderMethods.create_order(self, payload, access_token= 'invalid_token')
        assert status == 403, f'Ожидали 403, а получили {status}'
        assert response.json().get("success") is False, f'Ожидали success: true, получили {response}'

    @allure.title('Тест создания заказа без ингредиентов с авторизацией')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем создает заказ без ингредиентов'
                        'для этого юзера и проверяет, что сервер ответил 400 ошибкой')
    def test_create_new_empty_order_with_auth(self, create_user_and_delete):
        _, _, _, access_token = create_user_and_delete
        payload = EMPTY_ORDER
        response, status = OrderMethods.create_order(self, payload, access_token)
        assert status == 400, f'Ожидали 400, а получили {status}'
        assert response.json().get("success") is False, f'Ожидали success: false, получили {response}'

    @allure.title('Тест создания заказа c неверным хэшем продуктов с авторизацией')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем создает заказ с неверным хэшем продуктов'
                        'для этого юзера и проверяет, что сервер ответил 500 ошибкой')
    def test_create_new_invalid_order_with_auth(self, create_user_and_delete):
        _, _, _, access_token = create_user_and_delete
        payload = INVALID_ORDER
        response, status = OrderMethods.create_order(self, payload, access_token)
        assert status == 500, f'Ожидали 500, а получили {status}'
