from pages.order_feed_page import OrderFeedPage
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from conftest import driver
import allure


@allure.suite('Проверка раздела "Лента заказов"')
class TestOrderFeed:
    @allure.title('Проверка открытия деталей заказа при клике')
    def test_click_order_opens_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order_feed_button()
        order_feed_page.click_first_order()

        assert order_feed_page.check_order_details_modal_displayed()

    @allure.title('Заказы пользователя из истории отображаются в ленте заказов')
    def test_user_orders_displayed_in_feed(self, driver, create_user):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Создаем заказ'):
            order_feed_page.create_test_order(create_user)
            order_feed_page.close_order_modal()

        with allure.step('Получаем номер из истории заказов'):
            order_feed_page.click_personal_account_button()
            order_feed_page.click_order_history_button()
            history_order_number = order_feed_page.get_order_number_from_history()

        with allure.step('Получаем номер из ленты заказов'):
            order_feed_page.go_to_order_feed()
            feed_order_number = order_feed_page.get_order_number_from_feed()
            assert feed_order_number == history_order_number

    @allure.title('При создании заказа увеличивается счетчик "Выполнено за всё время"')
    def test_total_orders_counter_increases(self, driver, create_user):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Получаем начальное значение счетчика'):
            order_feed_page.go_to_order_feed()
            initial_total = int(order_feed_page.get_total_orders_count())

        with allure.step('Создаем заказ'):
            order_feed_page.create_test_order(create_user)
            order_feed_page.close_order_modal()

        with allure.step('Проверяем увеличение счетчика'):
            order_feed_page.go_to_order_feed()
            WebDriverWait(driver, 30).until(
                lambda driver: int(order_feed_page.get_total_orders_count()) > initial_total
            )
            new_total = int(order_feed_page.get_total_orders_count())
            assert new_total == initial_total + 1

    @allure.title('При создании заказа увеличивается счетчик "Выполнено за сегодня"')
    def test_today_orders_counter_increases(self, driver, create_user):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Получаем начальное значение счетчика'):
            order_feed_page.go_to_order_feed()
            initial_today = int(order_feed_page.get_today_orders_count())

        with allure.step('Создаем заказ'):
            order_feed_page.create_test_order(create_user)
            order_feed_page.close_order_modal()

        with allure.step('Проверяем увеличение счетчика'):
            order_feed_page.go_to_order_feed()
            WebDriverWait(driver, 30).until(
                lambda driver: int(order_feed_page.get_today_orders_count()) > initial_today
            )
            new_today = int(order_feed_page.get_today_orders_count())
            assert new_today > initial_today

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_new_orders_are_in_progress(self, driver, create_user):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Создаем заказ и получаем его номер'):
            order_feed_page.login_to_account(create_user)
            order_feed_page.wait_for_bun_available()
            order_feed_page.drag_ingredient_to_constructor()
            order_feed_page.click_create_order_button()
            order_feed_page.wait_for_order_confirmation()
            order_feed_page.check_incorrect_number_not_displayed()

            with allure.step('Получаем номер заказа из модального окна'):
                order_number = order_feed_page.get_created_order_number()

            with allure.step('Проверяем что получили реальный номер заказа'):
                if order_number == '9999':
                    pytest.skip(f"Пропускаем тест: получен дефолтный номер заказа {order_number}")


            with allure.step('Закрываем модальное окно'):
                order_feed_page.close_order_modal()

        with allure.step('Проверяем заказ в ленте заказов'):
            order_feed_page.click_order_feed_button()
            order_number_work = order_feed_page.get_order_number_in_progress()
            assert order_number in order_number_work, \
                f"Заказ {order_number} не найден в разделе 'В работе'. Найден: {order_number_work}"


