from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_cart(driver_logged):
    driver = driver_logged

    # Obtener el primer producto completo
    primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    # Obtener nombre del producto ANTES de agregarlo
    product_name = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Agregar producto al carrito
    primer_producto.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    # Verificar contador carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar el producto agregado en el carrito
    assert cart_item == product_name, "El producto agregado no coincide"