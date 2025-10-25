from playwright.sync_api import Page, expect
import csv
import re

class ProductPage:
    def __init__(self,page:Page):
        self.page=page
        #self.cart_icon="#shopping_cart_container"

    def add_item(self,xpath):
        self.page.locator(xpath).click()

        self.page.wait_for_timeout(3000)


    def add_to_cart(self):
        self.page.locator("a:has(svg[role='img'])").click()
        self.page.wait_for_timeout(3000)


    def add_thru_csv(self,csv_path):
        with open(csv_path,mode='r',encoding='utf-8-sig') as file:
            reader=csv.DictReader(file)
            print(reader.fieldnames)
            for row in reader:
                xpath= row['P_name']
                print(f"adding item:{xpath}")
                self.add_item(xpath)
