from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # === НАВИГАЦИЯ ===
    constructor_button = (By.XPATH, '//p[text()="Конструктор"]')
    order_feed_button = (By.XPATH, '//p[text()="Лента Заказов"]')
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # === ЛЕНТА ЗАКАЗОВ ===
    order_feed = (By.XPATH, '(//ul[contains(@class,"OrderFeed_list")]/li)[1]')
    order_number_feed = (By.XPATH, '(//p[contains(@class,"text_type_digits-default")])[1]')

    # === МОДАЛЬНЫЕ ОКНА ===
    order_info = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    modal_get_order = (By.XPATH, './/p[text()="Ваш заказ начали готовить"]')
    order_exit_button = (By.XPATH, '(//button[contains(@type,"button")])[1]')
    order_number = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    # === СОЗДАНИЕ ЗАКАЗА ===
    create_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    bun_R2_D3 = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    burger_area = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    assemble_burger = (By.XPATH, '//h1[text()="Соберите бургер"]')

    # === ЛИЧНЫЙ КАБИНЕТ И ИСТОРИЯ ===
    button_order_history = (By.XPATH, '//a[text()="История заказов"]')
    history_order = (By.XPATH, '//a[text()="История заказов"]')
    order_number_history = (By.XPATH, '//p[@class="text text_type_digits-default"]')

    # === СТАТИСТИКА ===
    order_all_time = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')
    order_today = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')
    order_number_work = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")

    # === АВТОРИЗАЦИЯ ===
    enter_email = (By.XPATH, '//input[@name="name"]')
    enter_password = (By.XPATH, '//input[@name="Пароль"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')

    # === ТЕСТОВЫЕ ДАННЫЕ ===
    incorrect_number = (By.XPATH, '//h2[contains(.,"9999")]')