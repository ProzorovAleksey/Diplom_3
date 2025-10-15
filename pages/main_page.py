from pages.base_page import BasePage
from locators.main_locators import MainPageLocators
import allure

class MainPage(BasePage):
    @allure.step('Вход в аккаунт')
    def login_to_account(self, user_data):
        email = user_data["email"]
        password = user_data["password"]

        self.click_element(MainPageLocators.button_personal_account)
        self.enter_text(MainPageLocators.enter_email, email)
        self.enter_text(MainPageLocators.enter_password, password)
        self.click_element(MainPageLocators.button_login)

    @allure.step('Клик по кнопке «Конструктор»')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.constructor_button)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.order_feed_button)

    @allure.step('Проверить наличие заголовка «Лента заказов»')
    def check_order_feed_title_displayed(self):
        return self.displaying_element(MainPageLocators.order_feed)

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

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient_to_constructor(self):
        browser_name = self.driver.capabilities['browserName'].lower()
        source = self.find_element(MainPageLocators.bun_R2_D3)
        target = self.find_element(MainPageLocators.burger_area)
        if browser_name == 'firefox':
            script = """
                    var source = arguments[0];
                    var target = arguments[1];

                    // Создаем события drag-and-drop
                    var dragStart = new Event('dragstart', { bubbles: true });
                    var dragOver = new Event('dragover', { bubbles: true });
                    var drop = new Event('drop', { bubbles: true });

                    source.dispatchEvent(dragStart);
                    target.dispatchEvent(dragOver);
                    target.dispatchEvent(drop);
                    """
            self.driver.execute_script(script, source, target)
        else:
            self.drag_and_drop_element(source, target)

    @allure.step('Получить количество ингредиентов')
    def get_ingredient_count(self):
        return self.get_text_element(MainPageLocators.count_bun)

    @allure.step('Ожидание доступности булочки')
    def wait_for_bun_available(self):
        self.wait_clickable_element(MainPageLocators.bun_R2_D3)

    @allure.step('Нажать кнопку «Оформить заказ»')
    def click_create_order(self):
        self.click_element(MainPageLocators.create_order)

    @allure.step('Проверить подтверждение заказа')
    def check_order_confirmation_displayed(self):
        return self.displaying_element(MainPageLocators.prep_order)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.get_url()
