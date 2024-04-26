from selenium.webdriver.common.by import By


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn")


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
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_EXIST = (By.CSS_SELECTOR, ".row:nth-child(1) h2")
    PRODUCT_NOT_EXIST = (By.CSS_SELECTOR, "#content_inner>p>a")
