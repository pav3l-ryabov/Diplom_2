import allure

from methods.user_methods import UserMethods


class TestPatchUser:

    @allure.title('Тест изменения данных пользователя с авторизацией')
    @allure.description('Тест создает юзера с валидными рандомными кредами, затем изменяет информацию о нем и новым запросом'
                        'проверяет, что информация действительно была изменена')
    def test_patch_user_with_auth(self, create_user_and_delete):
        email, password, name, access_token = create_user_and_delete
        payload = {
            "email": email + "test",
            "name": name + "test"
        }
        UserMethods.patch_user(self, payload, access_token)
        response, status = UserMethods.get_info_user(self, access_token)
        assert status == 200, f'Ожидали 200, получили {status}'
        assert all([
            response.json().get("success") is True,
            response.json().get("user", {}).get("email") == email + "test",
            response.json().get("user", {}).get("name") == name + "test"]), f'Ответ не соответствует ожидаемому: {response.json()}'

    @allure.title('Тест изменения данных пользователя без авторизации')
    @allure.description(
        'Тест создает юзера с валидными рандомными кредами, затем пытается изменить информацию о нем без авторизации'
        'и новым запросом проверяет, что информация изменена не была')
    def test_patch_user_without_auth(self, create_user_and_delete):
        email, password, name, access_token = create_user_and_delete
        payload = {
            "email": email + "test",
            "name": name + "test"
        }
        invalid_token_response, invalid_token_status = UserMethods.patch_user(self, payload, "invalid_token")
        get_info_response, get_info_status = UserMethods.get_info_user(self, access_token)
        assert [invalid_token_status == 403, get_info_status == 200], \
            f'Ожидали 403 и 200, а получили {invalid_token_status} и {get_info_status}'
        assert all([
            invalid_token_response.json().get("success") is False,
            get_info_response.json().get("success") is True,
            get_info_response.json().get("user", {}).get("email") == email,
            get_info_response.json().get("user", {}).get("name") == name]), \
            f'Ответ не соответствует ожидаемому: {response.json()}'