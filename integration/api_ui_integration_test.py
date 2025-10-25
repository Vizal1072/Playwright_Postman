import json

def read_token():
    with open("postman_api_tests/environment/reqres_env.json") as f:
        data = json.load(f)
        for item in data["values"]:
            if item["key"] == "token":
                return item["value"]
    return None

def test_api_then_ui(page):
    token = read_token()
    print("Token from API:", token)
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

