from pages.base_page import BasePage
from urls import Urls
from locators.main_locators import MainPageLocators
import allure

class MainPage(BasePage):
    @allure.step("Открываем главную страницу")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step('Кликаем на кнопку Войти в аккаунт')
    def click_enter_account_button(self):
        self.click_element(MainPageLocators.enter_account_button)


    @allure.step('Клик по кнопке «Лента заказов»')
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.order_feed_button)

    @allure.step('Клик по кнопке «Конструктор»')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.constructor_button)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_element(MainPageLocators.bun_R2_D3)

    @allure.step('Проверить открытие карточки ингредиента')
    def check_ingredient_info_displayed(self):
        return self.displaying_element(MainPageLocators.bun_R2_D3_info)

    @allure.step('Закрыть модальное окно')
    def click_close_modal(self):
        self.click_element(MainPageLocators.ingredient_modal_closed)

    @allure.step('Проверить закрытие модального окна')
    def check_modal_closed(self):
        return self.displaying_element(MainPageLocators.assemble_burger)

    @allure.step('Ожидание доступности булочки')
    def wait_for_bun_available(self):
        self.wait_clickable_element(MainPageLocators.bun_R2_D3)

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop_element(MainPageLocators.bun_R2_D3, MainPageLocators.burger_area)

    @allure.step('Получить количество ингредиентов')
    def get_ingredient_count(self):
        return self.get_text_element(MainPageLocators.count_bun)

    @allure.step('Ожидание подтверждения заказа')
    def wait_until_order_confirmed(self, timeout=15):
        self.wait_visibility_element(MainPageLocators.prep_order, timeout)

    @allure.step('Проверить отсутствие некорректного номера заказа')
    def check_incorrect_order_number_not_displayed(self):
        self.wait_until_element_invisible(MainPageLocators.incorrect_number)

    @allure.step('Вход в аккаунт')
    def login_to_account(self, user_data):
        email = user_data["email"]
        password = user_data["password"]

        self.click_element(MainPageLocators.button_personal_account)
        self.enter_text(MainPageLocators.enter_email, email)
        self.enter_text(MainPageLocators.enter_password, password)
        self.click_element(MainPageLocators.button_login)

    @allure.step('Нажать кнопку «Оформить заказ»')
    def click_create_order(self):
        self.click_element(MainPageLocators.create_order)

    @allure.step('Получить номер созданного заказа')
    def get_created_order_number(self):
        return self.get_text_element(MainPageLocators.order_number)

    @allure.step('Проверить подтверждение заказа')
    def check_order_confirmation_displayed(self):
        return self.displaying_element(MainPageLocators.prep_order)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_personal_account_button(self):
        self.wait_clickable_element(MainPageLocators.button_personal_account)
        self.click_element(MainPageLocators.button_personal_account)

    @allure.step('Нажимаем на Восстановить пароль')
    def click_restore_password(self):
        self.click_element(MainPageLocators.restore_password)
