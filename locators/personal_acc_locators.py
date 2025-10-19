from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    button_order_history = (By.XPATH, '//a[text()="История заказов"]')
    button_exit = (By.XPATH, '//button[text()="Выход"]')