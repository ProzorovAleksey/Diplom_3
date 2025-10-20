class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    CREATE_USER_URL = f"{BASE_URL}api/auth/register"
    USER_DELETE_URL = f'{BASE_URL}api/auth/user'
    FORGOT_PASSWORD = f'{BASE_URL}forgot-password'
    RESET_PASSWORD = f'{BASE_URL}reset-password'
    PROFILE = f'{BASE_URL}account/profile'
    HISTORY_ORDER = f'{BASE_URL}account/order-history'
    ORDER_FEED = f'{BASE_URL}feed'
    LOGIN_PAGE = f'{BASE_URL}login'