from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_full_checkout_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    overview = CheckoutOverviewPage(page)
    complete = CheckoutCompletePage(page)

    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory.assert_inventory_page_loaded()
    inventory.add_item_to_cart("Sauce Labs Bike Light")

    cart.open_cart()
    cart.assert_cart_loaded()
    cart.assert_item_in_cart("Sauce Labs Bike Light")

    checkout.start_checkout()
    checkout.fill_customer_info("Jane", "Doe", "90210")

    overview.assert_on_overview_page()
    overview.finish_checkout()

    complete.assert_checkout_complete()
