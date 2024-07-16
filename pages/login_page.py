from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.user_name = page.locator("#username")
        self.password = page.locator("#password")
        self.button = page.locator("#login")
        self.allert = page.locator("#errorAlert")

    def goto_login_page(self):
        self.page.goto("https://zimaev.github.io/pom/")

    def login(self, username: str, password: str):
        self.user_name.fill(username)
        self.password.fill(password)
        self.button.click()

    def get_messege(self, element):
        return element.inner_text()
    
    def get_error_messege(self):
        return self.get_messege(self.allert)
    
    def check_err_massege(self):
        expect(self.allert).to_have_text("Invalid credentials. Please try again.")
        #assert self.get_error_messege() == "Invalid credentials. Please try again."




