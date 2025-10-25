from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self,page:Page):
        self.page=page
        self.f_name="#first-name"
        self.l_name="#last-name"
        self.p_code="#postal-code"#postal-code
        self.c_button="#checkout_info_container > div > form > div.checkout_buttons > input"
        self.f_button="#checkout_summary_container > div > div.summary_info > div.cart_footer > a.btn_action.cart_button"

    def checkout(self):
        self.page.get_by_role("link", name="CHECKOUT").click()


    def fill_details(self,first,last,postal):
        self.page.fill(self.f_name,first)
        self.page.fill(self.l_name,last)
        self.page.fill(self.p_code,postal)
        self.page.click(self.c_button)


    def complete_order(self):
        self.page.click(self.f_button)
        self.page.wait_for_timeout(timeout=5000)