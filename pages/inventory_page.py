from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    # LOCATORS (privados)
    _TITLE = (By.CLASS_NAME, "app_logo")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _FILTER = (By.CLASS_NAME, "product_sort_container")
    _ADD_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)

    def menu_visible(self):
        return self.driver.find_element(*self._MENU_BUTTON).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self._FILTER).is_displayed()

    def agregar_primer_producto(self):
        self.driver.find_elements(*self._ADD_BUTTONS)[0].click()
        return self

    def obtener_contador_carrito(self):
        try:
            return int(self.driver.find_element(*self._CART_BADGE).text)
        except:
            return 0

    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self._PRODUCT_NAME)[0].text

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def agregar_producto_por_nombre(self,nombre_producto_json):
        productos = self.driver.find_elements(*self.inventory_items)

        for producto in productos:
            nombre = producto.find_element(*self.nombres_productos).text

            if nombre == nombre_producto_json:
                producto.find_element(*self.add_to_cart_buttons).click()

                break


