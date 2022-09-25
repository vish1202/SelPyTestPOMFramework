import pytest

from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.ProductPage import ProductPage
from pageObjects.CheckoutPage import CheckOut
from TestData.ProductPageData import ProductPageData
from pageObjects.CartPage import CartPage
from TestData.CartPageData import CartPageData
from TestData.CheckOutPageData import CheckOutPageData


class TestCheckout(BaseClass):

    @pytest.mark.cart
    @pytest.mark.depends(on="remove_cart_items")
    def test_verify_items_in_checkout_page(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        ProductPage.add_product_to_cart(self, "Sauce Labs Backpack").click()
        ProductPage.add_product_to_cart(self, "Sauce Labs Bike Light").click()
        ProductPage.go_to_cart(self).click()
        CheckOut.checkoutBtn(self).click()
        CheckOut.first_name(self).send_keys("Vishal")
        CheckOut.last_name(self).send_keys("Dewani")
        CheckOut.zip_code(self).send_keys(382345)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        assert "checkout-step-two.html" in self.driver.current_url

        products = CartPage.get_products_in_cart(self)
        product_list = []
        for product in products:
            items_to_add = product.text
            product_list.append(items_to_add)

        assert product_list == list(CartPageData.cart_items)

        item_prices = ProductPage.get_prices_of_items(self)
        price_list = []
        for price in item_prices:
            price_to_add = price.text
            price_list.append(price_to_add)

        assert price_list == list(CheckOutPageData.products_in_checkoutPage)

        sum_total_wo_tax = float(((price_list[0]).split('$'))[1]) + float(((price_list[1]).split('$'))[1])
        tax = 3.20
        assert sum_total_wo_tax + tax == 43.18

        self.driver.find_element(By.ID, "finish").click()
        assert "/checkout-complete.html" in self.driver.current_url
        order_success_msg = self.driver.find_element(By.CSS_SELECTOR, ".complete-header").text
        assert order_success_msg == 'THANK YOU FOR YOUR ORDER'
