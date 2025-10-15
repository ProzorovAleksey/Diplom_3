from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # === НАВИГАЦИЯ ===
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # === ЛИЧНЫЙ КАБИНЕТ ===
    profile = (By.XPATH, '//a[@href = "/account/profile"]')
    button_order_history = (By.XPATH, '//a[text()="История заказов"]')
    button_exit = (By.XPATH, '//button[text()="Выход"]')

    # === АВТОРИЗАЦИЯ ===
    enter_email = (By.XPATH, '//input[@name="name"]')
    enter_password = (By.XPATH, '//input[@name="Пароль"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')

    # === СОЗДАНИЕ ЗАКАЗА ===
    create_order = (By.XPATH, '//button[text()="Оформить заказ"]')