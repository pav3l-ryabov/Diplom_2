BASE_URL = 'https://stellarburgers.nomoreparties.site/'

REGISTER_USER_URL = 'api/auth/register'
LOGIN_USER_URL = 'api/auth/login'
DELETE_USER_URL = 'api/auth/user'

RESPONSE_BODY_EXIST_USER = {
    "success": False,
    "message": "User already exists"
}
RESPONSE_BODY_CREATE_USER_WITHOUT_FIELDS = {
    "success": False,
    "message": "Email, password and name are required fields"
}
DATA_TEST_REG_WITHOUT_FIELDS = [
        {"email": "email", "password": "", "name": ""},
        {"email": "", "password": "", "name": "name"},
        {"email": "email", "password": "", "name": "name"}
]