
from playwright_ui_tests.pages.login_page import LoginPage
from playwright_ui_tests.pages.products_page import ProductPage


def test_products_cart(page):

    page.goto("https://www.saucedemo.com/v1/")

    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    product_page=ProductPage(page)
    csv_path='playwright_ui_tests/utils/item.csv'
    product_page.add_thru_csv(csv_path)
    product_page.add_to_cart()




