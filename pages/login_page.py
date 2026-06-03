from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "https://www.saucedemo.com/"

    # LOCATORS 
    USER_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def completar_usuario(self, usuario):
        campo = self.wait.until(EC.visibility_of_element_located(self.USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)

    def completar_clave(self, clave):
        campo = self.driver.find_element(*self.PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)

    def hacer_clic_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, usuario, clave):
        self.abrir()
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()

    def obtener_mensaje_error(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
