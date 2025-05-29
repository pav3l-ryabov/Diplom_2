import requests
import random
import string

from data.data import BASE_URL, REGISTER_USER_URL

# взяли метод создающий юзера из 7 спринта, доработали:
# 1. Добавили функцию generate_random_email(length), которая генерирует email заданной длины
# 2. Переделали креды в payload под наш запрос
# 3. Добавили в return функции access_token, который забираем из ответа, он нужен, чтобы передать его в метод удаления
# юзера, который находится в фикстуре
def register_new_user_and_return_email_password_name():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(length):
        allowed_chars = string.ascii_lowercase + string.digits + "._%+-"
        first_part = ''.join(random.choice(allowed_chars) for _ in range(length))
        email = f"{first_part}@test.com"
        return email

    user_credentials = []

    email = generate_random_email(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f'{BASE_URL}{REGISTER_USER_URL}', data=payload)

    access_token = response.json()["accessToken"].split(" ")[1]

    if response.status_code == 200:
        user_credentials.append(email)
        user_credentials.append(password)
        user_credentials.append(name)
        user_credentials.append(access_token)

    return user_credentials

