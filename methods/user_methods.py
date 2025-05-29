import allure
import requests

from data.data import BASE_URL, REGISTER_USER_URL, LOGIN_USER_URL, DELETE_USER_URL


class UserMethods:

    @allure.step('Создание пользователя')
    def create_user(self, payload):
        response = requests.post(f'{BASE_URL}{REGISTER_USER_URL}', json = payload)
        return response, response.status_code

    @allure.step('Авторизация пользователя')
    def login_user(self, payload):
        response = requests.post(f'{BASE_URL}{LOGIN_USER_URL}', json = payload)
        return response, response.status_code

    @allure.step('Удаление пользователя')
    def delete_user(self, access_token):
        response = requests.delete(f'{BASE_URL}{DELETE_USER_URL}', headers={'Authorization': f'Bearer {access_token}'})
        return response, response.status_code