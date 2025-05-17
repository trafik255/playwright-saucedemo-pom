from playwright.sync_api import Page, expect

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.finish_button = page.locator("#finish")

    def assert_on_overview_page(self):
        expect(self.title).to_have_text("Checkout: Overview")

    def finish_checkout(self):
        self.finish_button.click()
