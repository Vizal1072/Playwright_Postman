
from playwright_ui_tests.pages.login_page import LoginPage
from playwright_ui_tests.pages.products_page import ProductPage
from playwright_ui_tests.pages.checkout_page import CheckoutPage


def test_checkout(page):

        page.goto("https://www.saucedemo.com/v1/")

        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")

        product_page = ProductPage(page)
        csv_path = 'playwright_ui_tests/utils/item.csv'
        product_page.add_thru_csv(csv_path)
        product_page.add_to_cart()

        checkout_page=CheckoutPage(page)
        checkout_page.checkout()
        checkout_page.fill_details("vizal","joseph","60001")
        checkout_page.complete_order()