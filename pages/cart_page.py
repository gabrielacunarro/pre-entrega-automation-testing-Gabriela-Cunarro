from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    # LOCATORS (privados)
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.url_contains("cart.html"))

    def obtener_items(self):
        """Devuelve los elementos HTML del carrito."""
        return self.driver.find_elements(*self._CART_ITEMS)

    def obtener_nombres(self):
        """Devuelve solo los nombres de los productos."""
        elementos = self.driver.find_elements(*self._ITEM_NAME)
        return [e.text for e in elementos]

    def obtener_productos(self):
        """
        Devuelve una lista de diccionarios:
        [
            {"nombre": "Sauce Labs Backpack", "precio": "$29.99"},
            {"nombre": "Bike Light", "precio": "$9.99"}
        ]
        """
        productos = []
        items = self.driver.find_elements(*self._CART_ITEMS)

        for item in items:
            nombre = item.find_element(*self._ITEM_NAME).text
            precio = item.find_element(*self._ITEM_PRICE).text

            productos.append({
                "nombre": nombre,
                "precio": precio
            })

        return productos

    def continuar_comprando(self):
        self.driver.find_element(*self._CONTINUE_SHOPPING).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def proceder_checkout(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()

