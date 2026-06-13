from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _PRODUCT_IMG = (By.CLASS_NAME, "inventory_item_img")
    _PRODUCT_DESC = (By.CLASS_NAME, "inventory_item_desc")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")

    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _FILTER = (By.CLASS_NAME, "product_sort_container")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text

    def obtener_productos(self):
        return self.driver.find_elements(*self._PRODUCTS)

    def obtener_primer_producto(self):
        return self.obtener_productos()[0]

    def obtener_nombre_primer_producto(self):
        return self.driver.find_elements(*self._PRODUCT_NAME)[0].text

    def obtener_precio_primer_producto(self):
        primer = self.obtener_primer_producto()
        return primer.find_element(*self._PRODUCT_PRICE).text

    def obtener_imagen_primer_producto(self):
        primer = self.obtener_primer_producto()
        return primer.find_element(*self._PRODUCT_IMG)

    def obtener_descripcion_primer_producto(self):
        primer = self.obtener_primer_producto()
        return primer.find_element(*self._PRODUCT_DESC).text

    def boton_add_visible(self):
        primer = self.obtener_primer_producto()
        return primer.find_element(*self._ADD_BUTTONS).is_displayed()

    def menu_visible(self):
        return self.driver.find_element(*self._MENU_BUTTON).is_displayed()

    def filtro_visible(self):
        return self.driver.find_element(*self._FILTER).is_displayed()

    def carrito_visible(self):
        return self.driver.find_element(*self._CART_LINK).is_displayed()

    def agregar_primer_producto(self):
        self.driver.find_elements(*self._ADD_BUTTONS)[0].click()
        return self

    def obtener_contador_carrito(self):
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_LINK).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def agregar_producto_por_nombre(self, nombre_producto):
        productos = self.driver.find_elements(*self._PRODUCTS)

        for producto in productos:
            nombre = producto.find_element(*self._PRODUCT_NAME).text

            if nombre == nombre_producto:
                boton = producto.find_element(*self._ADD_BUTTONS)
                boton.click()
                return True

        return False


    def hacer_logout(self):
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()

        from pages.login_page import LoginPage
        return LoginPage(self.driver)
