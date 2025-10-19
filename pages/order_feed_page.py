from selenium.common.exceptions import ElementClickInterceptedException
from urls import Urls
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import allure

class OrderFeedPage(BasePage):

    @allure.step('Получить номер заказа из ленты')
    def get_order_number_from_feed(self):
        return self.get_text_element(OrderFeedLocators.order_number_feed)

    @allure.step('Получить номер заказа из истории')
    def get_order_number_from_history(self):
        return self.get_text_element(OrderFeedLocators.order_number_history)

    @allure.step('Ожидание отображения счетчика всех заказов')
    def wait_until_total_orders_visible(self, timeout=10):
        self.wait_visibility_element(OrderFeedLocators.order_all_time, timeout)

    @allure.step('Ожидание отображения счетчика заказов за сегодня')
    def wait_until_today_orders_visible(self, timeout=10):
        self.wait_visibility_element(OrderFeedLocators.order_today, timeout)

    @allure.step('Получить количество заказов за сегодня')
    def get_today_orders_count(self):
        self.wait_clickable_element(OrderFeedLocators.order_today)
        return self.get_text_element(OrderFeedLocators.order_today)

    @allure.step('Получить количество заказов за всё время')
    def get_total_orders_count(self):
        self.wait_clickable_element(OrderFeedLocators.order_all_time)
        return self.get_text_element(OrderFeedLocators.order_all_time)

    @allure.step('Ожидание загрузки ленты заказов')
    def wait_until_order_feed_visible(self, timeout=10):
        self.wait_visibility_element(OrderFeedLocators.order_today, timeout)

    @allure.step('Получить номер заказа в работе')
    def get_order_number_in_progress(self):
        self.wait_clickable_element(OrderFeedLocators.order_number_work)
        return self.get_text_element(OrderFeedLocators.order_number_work)

    @allure.step('Перейти на страницу ленты заказов')
    def go_to_order_feed(self):
        self.open_page(Urls.ORDER_FEED)

    @allure.step('Проверить открытие окна деталей заказа')
    def check_order_details_modal_displayed(self):
        return self.displaying_element(OrderFeedLocators.order_info)

    @allure.step('Нажать на последний созданный заказ')
    def click_on_last_order(self):
        try:
            self.click_element(OrderFeedLocators.last_order)
        except ElementClickInterceptedException:
            # Если перехвачен, используем JavaScript клик
            self.click_element_with_js(OrderFeedLocators.last_order)

    @allure.step('Получить номер созданного заказа')
    def get_created_order_number(self):
        self.wait_visibility_element(OrderFeedLocators.order_number_title, timeout=10)
        self.wait_clickable_element(OrderFeedLocators.order_number_title)
        return self.get_text_element(OrderFeedLocators.order_number_title)
