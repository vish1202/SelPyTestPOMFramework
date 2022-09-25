import pytest

from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.ProductPage import ProductPage
from TestData.ProductPageData import ProductPageData
from pageObjects.CartPage import CartPage
from TestData.CartPageData import CartPageData


class TestProducts(BaseClass):

    @pytest.mark.tryfirst
    @pytest.mark.sort
    def test_verifysortAtoZ(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        self.getLogger().info("Selecting Name (Z to A) in sort drop down")
        self.selectdropdown_by_text("Name (Z to A)")
        self.getLogger().info("Fetching sorted items from products page")
        products = ProductPage.get_inventory_items(self)

        product_list = []
        for product in products:
            product_name = product.text
            product_list.append(product_name)
        self.getLogger().info("Verifying the sorting of items")
        assert list(ProductPageData.productsZtoA) == product_list

    @pytest.mark.sort
    def test_verifypriceHtoL(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        self.getLogger().info("Selecting Price (high to low) in sort drop down")
        self.selectdropdown_by_text("Price (high to low)")
        prices = ProductPage.get_prices_of_items(self)
        self.getLogger().info("Fetching sorted items from  products page")
        price_list = []
        for price in prices:
            item_price = price.text
            price_list.append(item_price)
        self.getLogger().info("Verifying sorted items from products page")
        assert list(ProductPageData.prices_high_to_low) == price_list

    @pytest.mark.depends(name="cart_count")
    @pytest.mark.cart
    def test_verifyaddtocart_count(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        self.getLogger().info("Adding items to cart")
        ProductPage.add_product_to_cart(self, "Sauce Labs Backpack").click()
        ProductPage.add_product_to_cart(self, "Sauce Labs Bike Light").click()
        self.getLogger().info("Verifying cart items count")
        cartcount = (ProductPage.get_cart_count(self)).text
        assert cartcount == '2'

    @pytest.mark.depends(on="cart_count")
    @pytest.mark.depends(name="cart_items_added")
    @pytest.mark.cart
    def test_verifyaddtocart_items(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        self.getLogger().info("Adding items to cart")
        ProductPage.add_product_to_cart(self, "Sauce Labs Backpack").click()
        ProductPage.add_product_to_cart(self, "Sauce Labs Bike Light").click()
        ProductPage.go_to_cart(self).click()
        assert '/cart.html' in self.driver.current_url
        self.getLogger().info("Fetching cart items displayed")
        cart_items = CartPage.get_products_in_cart(self)
        self.getLogger().info("Adding cart items to list")
        cart_items_list = []
        for item in cart_items:
            item_to_add = item.text
            cart_items_list.append(item_to_add)
        self.getLogger().info("verifying items from cart")
        assert cart_items_list == list(CartPageData.cart_items)

    @pytest.mark.depends(on="cart_items_added")
    @pytest.mark.depends(name="remove_cart_items")
    @pytest.mark.cart
    def test_verifyremovecart_items(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        ProductPage.go_to_cart(self).click()
        ProductPage.remove_item_from_cart(self, "Sauce Labs Backpack").click()
        cartcount = (ProductPage.get_cart_count(self)).text
        ProductPage.remove_item_from_cart(self, "Sauce Labs Bike Light").click()
        assert cartcount == '1'


