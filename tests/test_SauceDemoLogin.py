import pytest

from pageObjects.ProductPage import ProductPage
from utilities.BaseClass import BaseClass
from pageObjects.SauceDemoLoginPage import SauceDemoLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSauceLogin(BaseClass):

    def test_verifytitle(self):
        self.login_saucedemo("standard_user")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")))
        assert self.driver.title == "Swag Labs"

    def test_verifylockeduser(self):
        self.login_saucedemo("locked_out_user")
        assert SauceDemoLoginPage.lockedusermsg(self) == "Epic sadface: Sorry, this user has been locked out."

    def test_verifyperformanceuser(self):
        self.login_saucedemo("performance_glitch_user")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//span[text() = 'Products']")))
        assert "inventory.html" in self.driver.current_url

    @pytest.mark.trylast
    def test_verifylogout(self):
        self.login_saucedemo("standard_user")
        self.waitforpageload()
        self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        ProductPage.wait_for_left_nav_to_open(self)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
        self.driver.find_element(By.CSS_SELECTOR, "#logout_sidebar_link").click()
        assert "https://www.saucedemo.com/" == self.driver.current_url

    def test_verify_invalid_user(self):
        self.login_saucedemo("invalid_uname")
        invalid_user_msg = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert invalid_user_msg == 'Epic sadface: Username and password do not match any user in this service'