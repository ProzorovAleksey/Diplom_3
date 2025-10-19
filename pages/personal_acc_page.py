import allure
from locators.personal_acc_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Клик по кнопке «История заказов»')
    def click_order_history_button(self):
        self.click_element(PersonalAccountLocators.button_order_history)

    @allure.step('Клик по кнопке «Выход»')
    def click_logout_button(self):
        self.click_element(PersonalAccountLocators.button_exit)
        self.wait_until_element_invisible(PersonalAccountLocators.button_exit)
