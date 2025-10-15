from pages.base_page import BasePage
from locators.password_locators import PasswordLocators
import allure


class PasswordPage(BasePage):
    @allure.step('Клик по кнопке «Восстановить пароль»')
    def click_recovery_password_button(self):
        self.click_element(PasswordLocators.button_recovery_password)

    @allure.step('Ввод email')
    def enter_email(self, email):
        self.enter_text(PasswordLocators.new_email, email)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_restore_button(self):
        self.click_element(PasswordLocators.button_restore)

    @allure.step('Проверить наличие кнопки «Сохранить»')
    def check_save_button_displayed(self):
        return self.displaying_element(PasswordLocators.button_save)

    @allure.step('Ожидание появления кнопки «Сохранить»')
    def wait_for_save_button(self):
        return self.wait_visibility_element(PasswordLocators.button_save)

    @allure.step('Клик по иконке видимости пароля')
    def click_password_visibility_icon(self):
        self.click_element(PasswordLocators.icon_action_password)

    @allure.step('Проверить активность поля пароля')
    def is_password_field_active(self):
        return self.displaying_element(PasswordLocators.new_password)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.get_url()

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_personal_account_button(self):
        self.click_element(PasswordLocators.button_personal_account)

    @allure.step('Восстановить пароль для email')
    def recover_password(self, email):
        self.click_recovery_password_button()
        self.enter_email(email)
        self.click_restore_button()
        return self.wait_for_save_button()