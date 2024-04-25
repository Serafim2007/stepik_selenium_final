from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_empty_message()
        self.should_be_product_not_present()

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_NOT_EXIST), "Product add to basket but not should"

    def should_be_product_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_EXIST), "Product add to basket but not should"
