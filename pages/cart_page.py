from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    # LOCATORS
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.url_contains("cart.html"))

    def obtener_productos_en_carrito(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def obtener_nombres_productos(self):
        elementos = self.driver.find_elements(*self.ITEM_NAMES)
        return [e.text for e in elementos]

    def continuar_comprando(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def proceder_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
