import pytest 
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://www.saucedemo.com/")
    yield driver
    driver.quit()