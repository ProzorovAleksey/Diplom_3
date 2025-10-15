from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента")
    def wait_visibility_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента")
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait_clickable_element(locator)
        element.click()

    @allure.step("Ввести текст")
    def enter_text(self, locator, text):
        element = self.wait_visibility_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text_element(self, locator):
        element = self.wait_visibility_element(locator)
        return element.text

    @allure.step("Получить текущий URL")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Проверить отображение элемента")
    def displaying_element(self, locator):
        try:
            return self.wait_visibility_element(locator, timeout=5).is_displayed()
        except:
            return False

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Drag-and-drop")
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    @allure.step("Ожидание скрытия элемента {locator}")
    def wait_until_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))

    @allure.step("Перейти на URL")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()