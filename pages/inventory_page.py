from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.items = page.locator(".inventory_item")

    def assert_inventory_page_loaded(self):
        expect(self.title).to_have_text("Products")
        expect(self.items).to_have_count_above(0)

    def add_item_to_cart(self, item_name: str):
        self.page.locator(".inventory_item", has_text=item_name).locator("button").click()
