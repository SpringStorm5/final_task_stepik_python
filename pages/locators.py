from imp import SEARCH_ERROR
from selenium.webdriver.common.by import By
class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    CURRENT_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class LoginPageLocators(object):
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    USER_REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    USER_REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    USER_REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    USER_REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    INFO_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    INFO_MESSAGE_CART_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong") 
    #PRICE_BASKET = 
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CLASS_NAME, "icon-user")

class CartPageLocators(object):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "div.content div#content_inner p")
    ITEM_IN_CART = (By.CSS_SELECTOR, "div.basket-items .row")

class VendPageLocators(object):
    SEARCH_BUTTONMAIN = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[7]/div[1]")
    SEARCH_INPUT = (By.NAME, "q")
    CATALOG_BUTTON = (By.ID, "catalogue-button-desktop")
    SEARCH_BUTTON = (By.CLASS_NAME, "pure-button search-submit")

        


        