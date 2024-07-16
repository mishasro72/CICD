import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time
import allure

URL = "https://zimaev.github.io/pom/"
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Authorization")
@allure.title("Negative login testing")
def test_login(page):
    with allure.step("Create a Login Page object"):
        login_page = LoginPage(page)
    with allure.step("Open an authorization page"):
        login_page.goto_login_page()
    with allure.step("Login using invalid credentials"):
        login_page.login("user", "password")
    with allure.step("Chech the error message"):
        login_page.check_err_massege()
    time.sleep(3)

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.title("Positiv login testing")
def test_dashboard(page):
    cur_page = LoginPage(page)
    cur_page.goto_login_page()
    cur_page.login("admin", "admin")
    cur_page = DashboardPage(page)
    cur_page.chech_welc_messege()
    time.sleep(3)
