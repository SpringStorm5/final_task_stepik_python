from selenium.common.exceptions import *
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium import webdriver
from .pages.cart_page import CartPage
import time
import pytest 
LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# def test_guest_can_add_product_to_cart(browser):
#   link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#   page = ProductPage(browser, link)
#   page.open()
#   page.add_to_basket()
#   page.solve_quiz_and_get_code()
#   page.should_be_product_add_basket()
#   #print('Товар + print(productname) + добавлен в корзину')
#   page.should_priceproduct_equal_basket()
#   #print('Стоимость корзины print')
#   #time.sleep(60)
#   #result = page.solve_quiz_and_get_code()
#   #print(result)

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_can_add_product_to_cart(browser, link):
#     # ваша реализация теста
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_product_add_basket()
#     print('Товар + print(productname) + добавлен в корзину')
#     page.should_priceproduct_equal_basket()
#     print('Стоимость корзины print')

# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.check_adding_message_not_present()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.go_to_login_page()
#     page = LoginPage(browser, browser.current_url)
#     page.should_be_login_url()
#     page.should_be_login_form()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_url()
    cart_page.cart_is_empty()
    cart_page.should_be_empty_cart_message()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.should_be_login_url()
    page.should_be_login_form()


# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.should_be_product_add_basket()
#     page.check_adding_message_not_present()

# def test_message_disappeared_after_adding_product_to_cart(browser):
#     page = ProductPage(browser, LINK)
#     page.open()
#     page.should_be_product_add_basket()
#     page.check_adding_message_is_disappeared()

