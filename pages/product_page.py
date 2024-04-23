import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_btn.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()

    def should_be_product_page(self):
        self.should_be_product_message()
        self.should_be_correct_product()
        self.should_be_price_message()
        self.should_be_correct_price()

    def should_be_product_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_MESSAGE), "Product message is not presented"

    def should_be_correct_product(self):
        assert (self.browser.find_element(*ProductPageLocators.ACTUAL_PRODUCT).text in
                self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT).text), "Product is incorrect"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), "Price message is not presented"

    def should_be_correct_price(self):
        assert (self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE).text in
                self.browser.find_element(*ProductPageLocators.CORRECT_PRICE).text), "Price is incorrect"
