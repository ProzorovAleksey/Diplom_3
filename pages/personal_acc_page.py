import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.personal_acc_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    def _click_with_fallback(self, locator):
        browser_name = self.driver.capabilities['browserName'].lower()

        if browser_name == 'firefox':
            element = self.wait_visibility_element(locator, timeout=15)
            self.driver.execute_script("arguments[0].click();", element)
        else:
            try:
                self.wait_clickable_element(locator, timeout=10)
                self.click_element(locator)
            except ElementClickInterceptedException:
                element = self.find_element(locator)
                self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Вход в аккаунт')
    def login_to_account(self, user_data):
        email = user_data["email"]
        password = user_data["password"]

        self.click_personal_account_button()
        self.enter_text(PersonalAccountLocators.enter_email, email)
        self.enter_text(PersonalAccountLocators.enter_password, password)
        self.click_login_button()
        self.wait_visibility_element((PersonalAccountLocators.create_order), timeout=10)

    @allure.step('Клик по кнопке «Войти»')
    def click_login_button(self):
        self._click_with_fallback(PersonalAccountLocators.button_login)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_personal_account_button(self):
        self._click_with_fallback(PersonalAccountLocators.button_personal_account)

    @allure.step('Ожидание кнопки «Профиль»')
    def wait_for_profile_button(self):
        browser_name = self.driver.capabilities['browserName'].lower()

        if browser_name == 'firefox':
            return self.wait_visibility_element(PersonalAccountLocators.profile, timeout=15)
        else:
            return self.wait_clickable_element(PersonalAccountLocators.profile, timeout=10)

    @allure.step('Клик по кнопке «История заказов»')
    def click_order_history_button(self):
        self._click_with_fallback(PersonalAccountLocators.button_order_history)

    @allure.step('Клик по кнопке «Выход»')
    def click_logout_button(self):
        self._click_with_fallback(PersonalAccountLocators.button_exit)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.get_url()

    @allure.step('Проверить что пользователь в личном кабинете')
    def is_personal_account_loaded(self):
        browser_name = self.driver.capabilities['browserName'].lower()

        if browser_name == 'firefox':
            current_url = self.get_current_url()
            is_correct_url = "/account" in current_url
            has_profile_element = self.displaying_element(PersonalAccountLocators.profile)
            return is_correct_url and has_profile_element
        else:
            return self.displaying_element(PersonalAccountLocators.profile)

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click_logout_button()
        self.wait_visibility_element(PersonalAccountLocators.button_login, timeout=10)