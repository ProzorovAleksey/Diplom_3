from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import allure


class BasePage:
    @allure.title('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

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

    @allure.step('Открываем заданную страницу по URL с ожиданием ее загрузки')
    def open_page(self, url):
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

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
    def drag_and_drop_element(self, source_locator, target_locator):
        browser_name = self.driver.capabilities['browserName'].lower()
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        if browser_name == 'firefox':
            script = """
                var source = arguments[0];
                var target = arguments[1];
                var dragStart = new Event('dragstart', { bubbles: true });
                var dragOver = new Event('dragover', { bubbles: true });
                var drop = new Event('drop', { bubbles: true });
                source.dispatchEvent(dragStart);
                target.dispatchEvent(dragOver);
                target.dispatchEvent(drop);
            """
            self.driver.execute_script(script, source, target)
        else:
            ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Ожидание скрытия элемента {locator}")
    def wait_until_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))


    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Ожидание увеличения числового значения")
    def wait_for_value_increase(self, get_value_function, initial_value, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: int(get_value_function()) > initial_value
        )

    @allure.step('Кликнуть на элемент с помощью JavaScript')
    def click_element_with_js(self, locator):
        """Клик на элемент с помощью JavaScript, обходя обычные ограничения"""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Кликнуть на элемент с fallback на JavaScript')
    def click_element_with_js_fallback(self, locator):
        """Пытается кликнуть обычным способом, при ошибке использует JavaScript"""
        try:
            self.click_element(locator)
        except ElementClickInterceptedException:
            self.click_element_with_js(locator)