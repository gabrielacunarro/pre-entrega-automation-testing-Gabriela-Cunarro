from src.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito(driver):
    login(driver)

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos visibles."
    primer_producto = productos[0]

    # Obtener nombre del producto.
    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Hacer click en add to cart del primer producto.
    boton_add = primer_producto.find_element(By.TAG_NAME, "button")
    boton_add.click()

    # Esperar a que aparezca el contador del carrito.
    carrito = driver.find_element(By.ID, "shopping_cart_container")

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    contador = carrito.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1", "El contador del carrito no se incrementó correctamente."

    # Navegar al carrito.
    carrito.click()

    # Verificar que el producto esté en el carrito.
    item_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_carrito == nombre_producto, "El producto del carrito no coincide con el agregado."
