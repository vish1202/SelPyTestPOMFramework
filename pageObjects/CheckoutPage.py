from selenium.webdriver.common.by import By


class CheckOut:

    def __init__(self, driver):
        self.driver = driver

    cards = (By.XPATH, "//div[@class='card h-100']")
    checkout_btn = (By.XPATH, "//button[@id='checkout']")
    firstname = (By.XPATH, "//input[@id='first-name']")
    lastname = (By.XPATH, "//input[@id='last-name']")
    zipcode = (By.XPATH, "//input[@id='postal-code']")

    def getCards(self):
        return self.driver.find_elements(*CheckOut.cards)

    def checkoutBtn(self):
        return self.driver.find_element(*CheckOut.checkout_btn)

    def first_name(self):
        return self.driver.find_element(*CheckOut.firstname)

    def last_name(self):
        return self.driver.find_element(*CheckOut.lastname)

    def zip_code(self):
        return self.driver.find_element(*CheckOut.zipcode)
