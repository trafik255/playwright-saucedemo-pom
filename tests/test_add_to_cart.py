from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_single_item_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory.assert_inventory_page_loaded()
    inventory.add_item_to_cart("Sauce Labs Backpack")

    cart.open_cart()
    cart.assert_cart_loaded()
    cart.assert_item_in_cart("Sauce Labs Backpack")
