BASE_URL = 'https://stellarburgers.nomoreparties.site/'

REGISTER_USER_URL = 'api/auth/register'
LOGIN_USER_URL = 'api/auth/login'
DELETE_USER_URL = 'api/auth/user'

ORDERS_URL = '/api/orders'

RESPONSE_BODY_EXIST_USER = {
    "success": False,
    "message": "User already exists"
}
RESPONSE_BODY_CREATE_USER_WITHOUT_FIELDS = {
    "success": False,
    "message": "Email, password and name are required fields"
}
RESPONSE_BODY_AUTH_USER_WITH_INVALID_CREDS = {
    "success": False,
    "message": "email or password are incorrect"
}
DATA_TEST_REG_WITHOUT_FIELDS = [
        {"email": "email", "password": "", "name": ""},
        {"email": "", "password": "", "name": "name"},
        {"email": "email", "password": "", "name": "name"}
]

VALID_ORDER = {"ingredients": ["61c0c5a71d1f82001bdaaa73"]}
EMPTY_ORDER = {"ingredients": []}
INVALID_ORDER = {"ingredients": ["invalid_hash142142"]}