from playwright.sync_api import Page, expect


class DashboardPage():

    def __init__(self, page: Page):
        self.page = page
        self.welc_messege = page.locator("#usernameDisplay")

    def chech_welc_messege(self):
        expect(self.welc_messege).to_have_text("Welcome admin")
