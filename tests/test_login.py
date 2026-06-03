from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.login_page import LoginPage

def test_login_validation(driver):
    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.login("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url

def test_login_invalid(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user", "1234")

    error = login_page.obtener_mensaje_error()

    assert "Epic sadface: Username and password do not match any user in this service" in error