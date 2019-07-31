from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    """docstring for ClassName"""
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        
    def should_be_product_add_basket(self):
        productname = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        productname_in_busket = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME).text
        assert productname == productname_in_busket, "имя товара не совпадает с товаром в корзине"

    def should_priceproduct_equal_basket(self):
        price_basket = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_CART_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price_basket == product_price, "цена товара не совпадает с ценой в корзине"

    def check_adding_message_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME), "Product adding message must be absent"
    def check_adding_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME), "Product adding message must be disappeared"

        
            



        