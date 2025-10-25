from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username_input="#user-name"
        self.password_input="#password"
        self.login_button="#login-button"

    def login(self,username,password):
        self.page.fill(self.username_input,username)
        self.page.fill(self.password_input,password)
        self.page.click(self.login_button)