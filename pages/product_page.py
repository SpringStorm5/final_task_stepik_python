from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	"""docstring for ClassName"""
	def add_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

	# def should_be_equal_result():
	# # 	assert 	
	def should_be_product_add_basket(self):
		productname = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
		productname_in_busket = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME).text
		print(productname)
		print(productname_in_busket)
		assert productname == productname_in_busket, "test message"

	def should_priceproduct_equal_basket(self):
		price_basket = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE_CART_PRICE).text
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		print(price_basket)
		print(product_price)
		assert price_basket == product_price, "test two message"

	def check_adding_message_not_present(self):
		assert self.is_not_element_present(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME), "Product adding message must be absent"
	def check_adding_message_is_disappeared(self):
	   	assert self.is_disappeared(*ProductPageLocators.INFO_MESSAGE_PRODUCT_NAME), "Product adding message must be disappeared"

    	
    	    



		