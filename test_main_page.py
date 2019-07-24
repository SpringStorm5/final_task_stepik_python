from selenium.common.exceptions import *
from .pages.main_page import MainPage
from .pages .login_page import LoginPage
from selenium import webdriver
import time
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page1 = LoginPage(browser,link)
    page1.should_be_login_url()
    page1.should_be_login_form()
    page1.should_be_register_form()

