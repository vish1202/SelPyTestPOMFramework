from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    sortDrpDwnField = (By.XPATH, "//select[@class='product_sort_container']")
    inventory_items = (By.XPATH, "//div[@class='inventory_item_name']")
    prices = (By.XPATH, "//div[@class='inventory_item_price']")
    add_to_cart_for = "//div[text()='<text_replace>']//parent::a//parent::div[@class='inventory_item_label']//following-sibling::div[@class='pricebar']//button"
    cart_count = (By.XPATH, "//a[@class='shopping_cart_link']//span")
    cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    remove_cart_item_btn = "//div[text()='<text_replace>']//parent::a//parent::div//following-sibling::div[@class='item_pricebar']//button"

    def sortDrpDwn(self):
        return self.driver.find_element(*ProductPage.sortDrpDwnField)

    def get_inventory_items(self):
        return self.driver.find_elements(*ProductPage.inventory_items)

    def get_prices_of_items(self):
        return self.driver.find_elements(*ProductPage.prices)

    def add_product_to_cart(self, item):
        product_xpath = (ProductPage.add_to_cart_for.replace("<text_replace>", item))
        add_to_cart = (By.XPATH, product_xpath)
        return self.driver.find_element(*add_to_cart)

    def get_cart_count(self):
        return self.driver.find_element(*ProductPage.cart_count)

    def go_to_cart(self):
        return self.driver.find_element(*ProductPage.cart)

    def remove_item_from_cart(self, item):
        product_xpath = (ProductPage.remove_cart_item_btn.replace("<text_replace>", item))
        remove_from_cart = (By.XPATH, product_xpath)
        return self.driver.find_element(*remove_from_cart)

    def wait_for_left_nav_to_open(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(
            (By.XPATH, "//*[@class='bm-item-list']//parent::div//parent::div"), 'aria-hidden', 'false'))
