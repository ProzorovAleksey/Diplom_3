import pytest
import requests
from selenium import webdriver
from faker import Faker
from urls import Urls

@pytest.fixture(params=['firefox'])
def driver(request):
    browser_name = request.param
    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(options=webdriver.FirefoxOptions())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(Urls.BASE_URL)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_user():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    response = requests.post(Urls.CREATE_USER_URL, json=user_data)
    response_data = response.json()

    yield user_data

    if 'accessToken' in response_data:
        headers = {'Authorization': response_data['accessToken']}
        requests.delete(Urls.USER_DELETE_URL, headers=headers)