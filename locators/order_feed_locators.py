from selenium.webdriver.common.by import By


class OrderFeedLocators:

    order_number_title = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
    last_order = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
    order_info = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    order_all_time = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')
    order_today = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')
    order_number_work = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")
    order_number_history = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    order_number_feed = (By.XPATH, '(//div[contains(@class, "OrderFeed_order")])[1]//p[contains(text(), "#")]')