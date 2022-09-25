from selenium.webdriver.common.by import By


class SauceDemoLoginPage:

    def __init__(self, driver):
        self.driver = driver

    uname = (By.XPATH, "//input[@id='user-name']")
    pwd = (By.XPATH, "//input[@id='password']")
    loginbtn = (By.XPATH, "//input[@id='login-button']")
    lockeduser_msg = (By.XPATH, "//h3[@data-test='error']")

    def username(self):
        return self.driver.find_element(*SauceDemoLoginPage.uname)

    def password(self):
        return self.driver.find_element(*SauceDemoLoginPage.pwd)

    def loginBtn(self):
        return self.driver.find_element(*SauceDemoLoginPage.loginbtn)

    def lockedusermsg(self):
        return str(self.driver.find_element(*SauceDemoLoginPage.lockeduser_msg).text)