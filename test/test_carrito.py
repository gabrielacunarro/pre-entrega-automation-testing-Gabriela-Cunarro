import pytest
from src.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_carrito(driver):
    login(driver)

    # Cerrar popup si aparece
    try:
        driver.find_element(By.XPATH, "//button[text()='OK']").click()
    except:
        pass

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Botón robusto
    boton_add = primer_producto.find_element(By.TAG_NAME, "button")

    # Click forzado
    driver.execute_script("arguments[0].click();", boton_add)

    # Esperar badge
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    carrito = driver.find_element(By.ID, "shopping_cart_container")
    contador = carrito.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"

    carrito.click()

    item_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert item_carrito == nombre_producto
