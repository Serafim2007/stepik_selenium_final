from selenium.webdriver.common.by import By


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner")
    ACTUAL_PRODUCT = (By.CSS_SELECTOR, "#messages :nth-child(1) div strong")
    CORRECT_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")
    ACTUAL_PRICE = (By.CSS_SELECTOR, "#messages :nth-child(1)>strong")
    CORRECT_PRICE = (By.CSS_SELECTOR, ".product_main p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
