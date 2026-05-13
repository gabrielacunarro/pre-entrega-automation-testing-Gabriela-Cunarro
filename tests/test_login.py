import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_login(driver):
    login_page = LoginPage(driver)

    login_page.abrir().login_completo("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    inventory = InventoryPage(driver)
    assert inventory.obtener_titulo() == "Products"
