from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,args=["--start-maximized"])
        context=browser.new_context(no_viewport=True)
        yield context
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page=browser_context.new_page()
    yield page
    page.close()