from selenium.webdriver.common.by import By

class PasswordLocators:
    # === ЛИЧНЫЙ КАБИНЕТ ===
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # === ВОССТАНОВЛЕНИЕ ПАРОЛЯ ===
    button_recovery_password = (By.XPATH, '//a[text()="Восстановить пароль"]')
    button_restore = (By.XPATH, '//button[text()="Восстановить"]')

    # === ФОРМЫ ВВОДА ===
    new_email = (By.XPATH, '//input[@name="name"]')
    new_password = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::div')

    # === ИКОНКИ И ДЕЙСТВИЯ ===
    icon_action_password = (By.XPATH, '//div[contains(@class, "input__icon-action")]//*[local-name()="svg"]')

    # === КНОПКИ ===
    button_save = (By.XPATH, '//button[text()="Сохранить"]')

