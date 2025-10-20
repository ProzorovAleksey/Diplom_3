from pages.main_page import MainPage
from conftest import driver
import allure
from urls import Urls


@allure.suite('Проверка основного функционала')
class TestMain:

    @allure.title('Переход по клику на "Конструктор"')
    def test_click_constructor(self, driver):

        main_page = MainPage(driver)
        main_page.click_constructor_button()

        assert main_page.get_url() == Urls.BASE_URL

    @allure.title('Переход по клику на "Лента заказов"')
    def test_click_order_feed(self, driver):

        main_page = MainPage(driver)
        main_page.click_order_feed_button()

        assert main_page.get_url() == Urls.ORDER_FEED

    @allure.title('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_click_ingredient(self, driver):

        main_page = MainPage(driver)
        main_page.click_ingredient()

        assert main_page.check_ingredient_info_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_ingredient_modal_closed(self, driver):

        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.click_close_modal()

        assert main_page.check_modal_closed()

    @allure.title('При добавлении ингредиента в заказ увеличивается счетчик')
    def test_ingredient_counter_increases(self, driver):

        main_page = MainPage(driver)
        main_page.wait_for_bun_available()
        main_page.drag_ingredient_to_constructor()

        assert int(main_page.get_ingredient_count()) == 2

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_authorized_user_can_create_order(self, driver, create_user):

        main_page = MainPage(driver)
        main_page.login_to_account(create_user)
        main_page.wait_for_bun_available()
        main_page.drag_ingredient_to_constructor()
        main_page.click_create_order()

        assert main_page.check_order_confirmation_displayed()