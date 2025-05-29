import allure
import requests

from data.data import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step('Создание заказа')
    def create_order(self, payload, access_token):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json = payload,
                                 headers={'Authorization': f'Bearer {access_token}'})
        return response, response.status_code

    @allure.step('Получение заказа конкретного пользователя')
    def get_order(self, access_token):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers={'Authorization': f'Bearer {access_token}'})
        return response, response.status_code