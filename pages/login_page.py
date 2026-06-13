from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    # LOCATORS
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # CONSTRUCTOR
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ACCIONES DE ALTO NIVEL
    def abrir(self):
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_password(self, password: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))
        campo.clear()
        campo.send_keys(password)
        return self

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()
        return self

    def login(self, usuario, password):
        self.abrir()  
        self.completar_usuario(usuario)
        self.completar_password(password)
        self.click_login()
        return self

    def esta_error_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False

    def obtener_mensaje_error(self):
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""
