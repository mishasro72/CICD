import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
import allure
import time

URL = "https://zimaev.github.io/pom/"

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Dashbord page")
@allure.title("Checking the number of main menu items")

def test_main_menu(page):
    dash_page = LoginPage(page)
    dash_page.goto_login_page()
    dash_page.login("admin", "admin")
    dash_page = DashboardPage(page)
    print(f"""\n{dash_page.count_items('//div[@class="list-group list-group-flush"]/*')}""")
    dash_page.check_number_of_menu_elem()



