from selenium.webdriver.common.by import By

class MainPageLocators:

    # === НАВИГАЦИЯ И ЗАГОЛОВКИ ===
    constructor_button = (By.XPATH, '//p[text()="Конструктор"]')
    order_feed_button = (By.XPATH, '//p[text()="Лента Заказов"]')
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Заголовки страниц
    order_feed = (By.XPATH, '//h1[text()="Лента Заказов"]')
    assemble_burger = (By.XPATH, '//h1[text()="Соберите бургер"]')

    # === ИНГРЕДИЕНТЫ И КОНСТРУКТОР ===
    # Ингредиенты
    bun_R2_D3 = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    bun_R2_D3_info = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    ingredient_details = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    count_bun = (By.XPATH, './/a[contains(@class, "BurgerIngredient_ingredient")]//p[contains(@class, "counter_counter__num")][1]')

    # Область конструктора
    burger_area = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # === МОДАЛЬНЫЕ ОКНА ===
    ingredient_modal_closed = (By.XPATH, '(//button[@type="button" and contains(@class, "Modal_modal__close_modified")])[1]')

    # === ФОРМЫ АВТОРИЗАЦИИ ===
    enter_email = (By.XPATH, '//input[@name="name"]')
    enter_password = (By.XPATH, '//input[@name="Пароль"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')
    profile = (By.XPATH, '//a[text()="Профиль"]')

    # === ЗАКАЗЫ ===
    create_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    prep_order = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')