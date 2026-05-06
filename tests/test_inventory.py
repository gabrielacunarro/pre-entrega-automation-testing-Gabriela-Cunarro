from src.helpers import login
from selenium.webdriver.common.by import By

def test_invetory(driver):
    #Login (valida URL y titulo)
    login(driver)

    #Verificar que existan prodcutos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos visibles en el inventario."

    #Obtener nombre y precio del primer producto
    primer_producto = productos[0]

    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    imagen = primer_producto.find_element(By.CLASS_NAME, "inventory_item_img")
    descripcion = primer_producto.find_element(By.CLASS_NAME, "inventory_item_desc").text
    boton_add = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
    
    assert nombre != "" , "El primer producto no tiene nombre."
    assert precio != "" , "El primer producto no tiene precio."
    assert imagen.is_displayed(), "El primer producto no tiene imagen."
    assert descripcion != "" , "El primer producto no tiene descripcion."
    assert boton_add.is_displayed(), "El boton de agregar al carrito no es visible."

    #Validar elementos importantes (menu, filtro, cart)
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    carrito = driver.find_element(By.ID, "shopping_cart_container")

    assert menu.is_displayed(), "El menu no es visible."
    assert filtro.is_displayed(), "El filtro no es visible."
    assert carrito.is_displayed(), "El carrito no es visible."
