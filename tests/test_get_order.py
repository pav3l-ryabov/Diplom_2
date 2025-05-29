import allure

from methods.order_methods import OrderMethods


class TestGetOrder:

    @allure.title('Тест получения заказа с авторизацией')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем проверяет его заказ что сервер ответил корректно')
    def test_get_order_with_auth(self, create_user_and_delete):
        _, _, _, access_token = create_user_and_delete
        response, status = OrderMethods.get_order(self, access_token)
        assert status == 200, f'Ожидали 200, а получили {status}'
        assert response.json().get("success") is True, f'Ожидали success: true, получили {response}'

    @allure.title('Тест получения заказа с неправильным токеном')
    @allure.description('Тест пытается получить заказ с невалидным токеном')
    #убрал фикстуру create_user_and_delete, т.к. в этом тесте в ней нет смысла, мы ничего не передаем, кроме
    #заведомо неправильного токена
    def test_get_order_without_auth(self):
        response, status = OrderMethods.get_order(self, access_token = 'invalid_token')
        assert status == 403, f'Ожидали 403, а получили {status}'
        assert response.json().get("success") is False, f'Ожидали success: false, получили {response}'