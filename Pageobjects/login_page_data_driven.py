# import time
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from Utilities.base_driver import basedriver


class login_page_ddt(basedriver):
    # all the locators  from login page
    username = "username"
    password = "password"
    submitBtn = "//button[text()='Submit']"
    Invalid_cred = "//section[@id='main-container']//div[text()='Your username is invalid!']"
    url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_url(self):
        self.driver.get(self.url)

    def get_username(self):
        return self.wait_until_element_is_clickable(By.NAME, self.username)

    def enter_username(self, user_name):
        self.get_username().clear()
        self.get_username().send_keys(user_name)
        self.get_username().send_keys(Keys.ENTER)

    def get_password(self):
        return self.wait_until_element_is_clickable(By.NAME, self.password)

    def enter_password(self, pass_word):
        self.get_password().clear()
        self.get_password().send_keys(pass_word)
        self.get_password().send_keys(Keys.ENTER)

    def click_submit(self):
        self.wait_until_element_is_clickable(By.XPATH, self.submitBtn).click()

    def invalid_user(self):
        self.wait_until_element_is_visible(By.XPATH, self.Invalid_cred).is_displayed()

    def ele(self):
        self.driver.find_element_by_xpath(self.Invalid_cred)
        # ele1.text


class home_page(basedriver): # basedriver is called to get functions from basedriver.py which have webdriver wait custom methods
    # home page locators
    loginSuccess = "//*[text()='Logged In Successfully']"
    logout = "//*[text()='Log out']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_success(self):
        self.wait_until_element_is_visible(By.XPATH, self.loginSuccess)

    def log_out(self):
        self.wait_until_element_is_clickable(By.XPATH, self.loginSuccess).click()

