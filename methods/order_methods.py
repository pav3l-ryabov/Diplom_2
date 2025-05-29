import allure
import requests

from data.data import BASE_URL, LOGIN_USER_URL, DELETE_USER_URL, ORDERS_URL


class OrderMethods:

    @allure.step('Создание заказа')
    def create_order(self, payload, access_token):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json = payload,
                                 headers={'Authorization': f'Bearer {access_token}'})
        return response, response.status_code

    # @allure.step('Авторизация пользователя')
    # def login_user(self, payload):
    #     response = requests.post(f'{BASE_URL}{LOGIN_USER_URL}', json = payload)
    #     return response, response.status_code
    #
    # @allure.step('Удаление пользователя')
    # def delete_user(self, access_token):
    #     response = requests.delete(f'{BASE_URL}{DELETE_USER_URL}', headers={'Authorization': f'Bearer {access_token}'})
    #     return response, response.status_code
    #
    # @allure.step('Изменение данных пользователя')
    # def patch_user(self, payload, access_token):
    #     response = requests.patch(f'{BASE_URL}{DELETE_USER_URL}', json = payload,
    #                               headers={'Authorization': f'Bearer {access_token}'})
    #     return response, response.status_code
    #
    # @allure.step('Получение данных пользователя')
    # def get_info_user(self, access_token):
    #     response = requests.get(f'{BASE_URL}{DELETE_USER_URL}', headers={'Authorization': f'Bearer {access_token}'})
    #     return response, response.status_code