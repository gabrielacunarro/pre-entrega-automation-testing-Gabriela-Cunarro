from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    # LOCATORS
    TITLE = (By.CLASS_NAME, "app_logo")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    FILTER = (By.CLASS_NAME, "product_sort_container")
    ADD_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.driver.find_element(*self.TITLE).text

    def obtener_productos(self):
        return self.driver.find_elements(*self.PRODUCTS)

    def menu_visible(self):
        return self.driver.find_element(*self.MENU_BUTTON).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self.FILTER).is_displayed()

    def agregar_producto_al_carrito(self):
        self.driver.find_elements(*self.ADD_BUTTONS)[0].click()

    def obtener_contador_carrito(self):
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except:
            return 0

    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self.PRODUCT_NAME)[0].text

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_LINK).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)
