from selenium.webdriver.common.by import By

class PasswordLocators:

    button_restore = (By.XPATH, '//button[text()="Восстановить"]')
    new_email = (By.XPATH, '//input[@name="name"]')
    new_password = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::div')
    icon_action_password = (By.XPATH, '//div[contains(@class, "input__icon-action")]//*[local-name()="svg"]')
    button_save = (By.XPATH, '//button[text()="Сохранить"]')

