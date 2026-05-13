from selenium.webdriver.common.by import By
import time

def login(driver):
    driver.get("https://www.saucedemo.com/") 

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    time.sleep(2)

    assert "/inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
