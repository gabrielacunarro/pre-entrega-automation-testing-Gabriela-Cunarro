import pytest 
from selenium import webdriver

@pytest.fixture()
def test_driver():
    driver = webdriver.Chrome()
    driver.get("http://www.saucedemo.com/")
    yield driver
    driver.quit()