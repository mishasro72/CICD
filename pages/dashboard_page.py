from playwright.sync_api import Page, expect


class DashboardPage():

    def __init__(self, page: Page):
        self.page = page
        self.welc_messege = page.locator("#usernameDisplay")
        self.main_menu = page.locator('//div[@class="list-group list-group-flush"]/*')

    def chech_welc_messege(self):
        expect(self.welc_messege).to_have_text("Welcome admin")

    def count_items(self, locator: str):
        return self.page.locator(locator).count()
    
    def check_number_of_menu_elem(self):
        expect(self.main_menu).to_have_count(5)


