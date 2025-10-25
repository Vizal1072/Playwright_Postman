from playwright.sync_api import sync_playwright
from playwright_ui_tests.pages.login_page import LoginPage

def test_login_success(page):
    page.goto("https://www.saucedemo.com/v1/")

    login_page=LoginPage(page)
    login_page.login("standard_user","secret_sauce")

    assert "inventory" in page.url
    print("login page successfully entered")

