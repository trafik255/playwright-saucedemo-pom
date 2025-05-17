from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")

    def open_cart(self):
        self.cart_icon.click()

    def assert_cart_loaded(self):
        expect(self.cart_title).to_have_text("Your Cart")

    def assert_item_in_cart(self, item_name: str):
        expect(self.page.locator(".inventory_item_name", has_text=item_name)).to_be_visible()
