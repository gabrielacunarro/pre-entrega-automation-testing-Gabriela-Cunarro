from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=Service())
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()
