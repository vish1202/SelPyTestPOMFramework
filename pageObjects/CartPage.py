from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    inventory_items = (By.XPATH, "//div[@class='inventory_item_name']")

    def get_products_in_cart(self):
        return self.driver.find_elements(*CartPage.inventory_items)
