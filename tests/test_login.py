from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.assert_inventory_page_loaded()
