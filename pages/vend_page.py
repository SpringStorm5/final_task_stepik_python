from time import sleep
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import VendPageLocators

class VendMagPage(BasePage):
    """docstring for ClassName"""

    def check_url(self):
       print(self.browser.current_url)
       assert "/www.vend-mag.ru" in self.browser.current_url, "Current URL is not vendmag URL"

    def search_vendmag(self):
        self.browser.find_element(*VendPageLocators.SEARCH_BUTTONMAIN).click()
        sleep(5)
        self.browser.find_element(*VendPageLocators.SEARCH_INPUT).send_keys('test')
        self.browser.find_element(*VendPageLocators.SEARCH_BUTTON).click()

    def click_catalog(self):
        self.browser.find_element(*VendPageLocators.CATALOG_BUTTON).click()

