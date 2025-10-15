from pages.personal_acc_page import PersonalAccountPage
from conftest import driver
import allure
from urls import Urls


@allure.suite('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Переход по клику на "Личный кабинет"')
    def test_navigate_to_personal_account(self, driver, create_user):
        personal_account_page = PersonalAccountPage(driver)

        with allure.step('Логинимся и переходим в личный кабинет'):
            personal_account_page.login_to_account(create_user)
            personal_account_page.click_personal_account_button()
            personal_account_page.wait_for_profile_button()

        with allure.step('Проверяем что загрузился личный кабинет'):
            assert personal_account_page.get_current_url() == Urls.PROFILE

    @allure.title('Переход в раздел "История заказов"')
    def test_navigate_to_order_history(self, driver, create_user):
        personal_account_page = PersonalAccountPage(driver)

        with allure.step('Логинимся и переходим в историю заказов'):
            personal_account_page.login_to_account(create_user)
            personal_account_page.click_personal_account_button()
            personal_account_page.wait_for_profile_button()
            personal_account_page.click_order_history_button()

        with allure.step('Проверяем что перешли в историю заказов'):
            assert personal_account_page.get_url() == Urls.HISTORY_ORDER

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver, create_user):
        personal_account_page = PersonalAccountPage(driver)

        with allure.step('Логинимся и выходим из аккаунта'):
            personal_account_page.login_to_account(create_user)
            personal_account_page.click_personal_account_button()
            personal_account_page.wait_for_profile_button()
            personal_account_page.logout()

        with allure.step('Проверяем выход из аккаунта'):
            assert personal_account_page.get_url() == Urls.LOGIN_PAGE