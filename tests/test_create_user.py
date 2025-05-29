import allure

from data.data import RESPONSE_BODY_EXIST_USER
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

