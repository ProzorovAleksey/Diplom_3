from pages.password_page import PasswordPage
from conftest import driver
import allure
from urls import Urls


@allure.suite('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_navigate_to_password_recovery_page(self, driver):
        password_page = PasswordPage(driver)
        password_page.click_personal_account_button()
        password_page.click_recovery_password_button()

        assert password_page.get_current_url() == Urls.FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    def test_email_input_and_recovery_flow(self, driver, create_user):
        password_page = PasswordPage(driver)
        user_data = create_user

        password_page.click_personal_account_button()
        password_page.click_recovery_password_button()
        password_page.enter_email(user_data["email"])
        password_page.click_restore_button()

        with allure.step('Ждем появления кнопки сохранения'):
            assert password_page.wait_for_save_button(), "Кнопка 'Сохранить' не появилась"
            assert password_page.get_current_url() == Urls.RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_password_visibility_toggle_activates_field(self, driver, create_user):
        password_page = PasswordPage(driver)
        user_data = create_user

        with allure.step('Восстанавливаем пароль'):
            password_page.click_personal_account_button()
            password_page.click_recovery_password_button()
            password_page.enter_email(user_data["email"])
            password_page.click_restore_button()
            password_page.wait_for_save_button()

        with allure.step('Кликаем на иконку видимости пароля'):
            password_page.click_password_visibility_icon()

        with allure.step('Проверяем что поле пароля активно'):
            assert password_page.is_password_field_active()