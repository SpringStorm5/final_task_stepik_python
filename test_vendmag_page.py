import pytest
import time
from selenium.common.exceptions import *
from .pages.vend_page import VendMagPage

from selenium import webdriver
import time

def test_search(browser):
    link = "https://www.vend-mag.ru/"
    page = VendMagPage(browser, link)
    page.open()
    page.check_url()
    page.click_catalog()
    page.search_vendmag()