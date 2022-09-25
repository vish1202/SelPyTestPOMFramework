import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
import pytest

from pageObjects.SauceDemoLoginPage import SauceDemoLoginPage
from pageObjects.ProductPage import ProductPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def login_saucedemo(self, username):
        self.driver.get("https://www.saucedemo.com/")
        login_obj = SauceDemoLoginPage(self.driver)
        login_obj.username().send_keys(username)
        login_obj.password().send_keys("secret_sauce")
        login_obj.loginBtn().click()

    def waitforpageload(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")))
        except Exception as e:
            print(e, "page did not load successfully")

    def selectdropdown_by_text(self, text):
        sel = Select(ProductPage.sortDrpDwn(self))
        sel.select_by_visible_text(text)

