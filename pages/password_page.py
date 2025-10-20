from pages.base_page import BasePage
from locators.password_locators import PasswordLocators
import allure


class PasswordPage(BasePage):

    @allure.step('Ввод email')
    def enter_email(self, email):
        self.enter_text(PasswordLocators.new_email, email)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_restore_button(self):
        self.click_element(PasswordLocators.button_restore)

    @allure.step('Ожидание появления кнопки «Сохранить»')
    def wait_for_save_button(self):
        return self.wait_visibility_element(PasswordLocators.button_save)

    @allure.step('Клик по иконке видимости пароля')
    def click_password_visibility_icon(self):
        self.click_element(PasswordLocators.icon_action_password)

    @allure.step('Проверить активность поля пароля')
    def is_password_field_active(self):
        return self.displaying_element(PasswordLocators.new_password)
