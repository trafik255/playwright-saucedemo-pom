from playwright.sync_api import Page, expect

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.thank_you = page.locator(".complete-header")

    def assert_checkout_complete(self):
        expect(self.title).to_have_text("Checkout: Complete!")
        expect(self.thank_you).to_have_text("Thank you for your order!")
