from urls import Urls
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure

class OrderFeedPage(BasePage):
    @allure.step('Вход в аккаунт')
    def login_to_account(self, user_data):
        email = user_data["email"]
        password = user_data["password"]

        self.click_element(OrderFeedLocators.button_personal_account)
        self.enter_text(OrderFeedLocators.enter_email, email)
        self.enter_text(OrderFeedLocators.enter_password, password)
        self.click_element(OrderFeedLocators.button_login)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_order_feed_button(self):
        self.click_element(OrderFeedLocators.order_feed_button)

    @allure.step('Клик по первому заказу в ленте')
    def click_first_order(self):
        self.wait_visibility_element(OrderFeedLocators.order_feed)
        self.click_element(OrderFeedLocators.order_feed)

    @allure.step('Проверить открытие окна деталей заказа')
    def check_order_details_modal_displayed(self):
        return self.displaying_element(OrderFeedLocators.order_info)

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient_to_constructor(self):
        source = self.find_element(OrderFeedLocators.bun_R2_D3)
        target = self.find_element(OrderFeedLocators.burger_area)
        self.drag_and_drop_element(source, target)

    @allure.step('Ожидание доступности булочки')
    def wait_for_bun_available(self):
        self.wait_clickable_element(OrderFeedLocators.bun_R2_D3)

    @allure.step('Нажать кнопку «Оформить заказ»')
    def click_create_order_button(self):
        self.click_element(OrderFeedLocators.create_order)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_personal_account_button(self):
        self.wait_clickable_element(OrderFeedLocators.button_personal_account)
        self.click_element(OrderFeedLocators.button_personal_account)

    @allure.step('Клик по кнопке «История заказов»')
    def click_order_history_button(self):
        self.wait_clickable_element(OrderFeedLocators.button_order_history)
        self.click_element(OrderFeedLocators.button_order_history)

    @allure.step('Закрыть окно деталей заказа')
    def close_order_modal(self):
        self.driver.refresh()
        self.wait_visibility_element((OrderFeedLocators.assemble_burger), timeout=10)

    @allure.step('Получить номер заказа из истории')
    def get_order_number_from_history(self):
        browser_name = self.driver.capabilities['browserName'].lower()

        if browser_name == 'firefox':
            self.wait_visibility_element(OrderFeedLocators.order_number_history, timeout=15)
            return self.get_text_element(OrderFeedLocators.order_number_history)
        else:
            self.wait_clickable_element(OrderFeedLocators.order_number_history, timeout=10)
            return self.get_text_element(OrderFeedLocators.order_number_history)

    @allure.step('Получить номер заказа из ленты')
    def get_order_number_from_feed(self):
        browser_name = self.driver.capabilities['browserName'].lower()

        if browser_name == 'firefox':
            self.wait_visibility_element(OrderFeedLocators.order_number_feed, timeout=15)
            return self.get_text_element(OrderFeedLocators.order_number_feed)
        else:
            self.wait_clickable_element(OrderFeedLocators.order_number_feed, timeout=10)
            return self.get_text_element(OrderFeedLocators.order_number_feed)

    @allure.step('Получить количество заказов за всё время')
    def get_total_orders_count(self):
        self.wait_clickable_element(OrderFeedLocators.order_all_time)
        return self.get_text_element(OrderFeedLocators.order_all_time)

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_count(self):
        self.wait_clickable_element(OrderFeedLocators.order_today)
        return self.get_text_element(OrderFeedLocators.order_today)

    @allure.step('Клик по кнопке «Конструктор»')
    def click_constructor_button(self):
        self.wait_clickable_element(OrderFeedLocators.constructor_button)
        self.click_element(OrderFeedLocators.constructor_button)

    @allure.step('Получить номер созданного заказа')
    def get_created_order_number(self):
        self.wait_visibility_element(OrderFeedLocators.order_number, timeout=10)
        self.wait_clickable_element(OrderFeedLocators.order_number)
        return self.get_text_element(OrderFeedLocators.order_number)

    @allure.step('Получить номер заказа в работе')
    def get_order_number_in_progress(self):
        self.wait_clickable_element(OrderFeedLocators.order_number_work)
        return self.get_text_element(OrderFeedLocators.order_number_work)

    @allure.step('Проверить отсутствие некорректного номера заказа')
    def check_incorrect_number_not_displayed(self):
        self.wait_until_element_invisible(OrderFeedLocators.incorrect_number)

    @allure.step('Ожидание подтверждения заказа')
    def wait_for_order_confirmation(self):
        self.wait_visibility_element(OrderFeedLocators.modal_get_order)

    @allure.step('Перейти на страницу ленты заказов')
    def go_to_order_feed(self):
        self.go_to_url(Urls.ORDER_FEED)


    @allure.step('Создать заказ для тестирования')
    def create_test_order(self, user_data):
        self.login_to_account(user_data)
        self.wait_for_bun_available()
        self.drag_ingredient_to_constructor()
        self.click_create_order_button()
        self.wait_for_order_confirmation()
        order_number = self.get_created_order_number()
        return order_number