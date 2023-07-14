import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import InvalidElementStateException
from Pageobjects.loginpage import Loginpage
from Utilities.Readproperties import readconfig
from Utilities.customLogger import loggen
from selenium import webdriver


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup")  # using pytest fixture to setup driver instances
class Test_001_Login:
    baseURL = readconfig.getApplicationURL()
    mobilenumber = readconfig.getmobilenumber()
    password = readconfig.getpassword()

    # baseURL="https://my.indiamart.com/"
    # mobilenumber="8333956091"
    # password="Hari@9911"
    logger = loggen()

    @pytest.fixture(autouse=True)  # This fixture will act as support to setup driver
    def class_setup(self):
        self.lp = Loginpage(self.driver)  # This is to create one variable and use it widely for login page

    @allure.severity(allure.severity_level.MINOR)
    def test_homePage_title(self):
        self.logger.info('****TestLogin****')
        self.logger.info('****Verifying home page title****')
        # self.driver = setup
        self.driver.get(self.baseURL)  # here we don't have loop hence we can use url from read-properties module
        act_title = self.driver.title
        if act_title == "IndiaMART - Indian Manufacturers Suppliers Exporters Directory,India Exporter Manufacturers":
            assert True
            self.driver.close()
            print("Title is validated")
            self.logger.info('****Home page title passed****')
        else:
            t = self.driver.title
            print("Title is Incorrect")
            print("This is the Page title: ", t)
            allure.attach(self.driver.get_screenshot_as_png(), name="Homepagetitle", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePage_title.png")
            self.driver.close()
            self.logger.error('****Home page title failed****')
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginpage(self):
        self.logger.info('****Verifying login test****')
        self.driver.get(self.baseURL)
        # handling exceptions using try except blocks
        try:
            self.lp.setmobilenumber(self.mobilenumber)
        except InvalidElementStateException:
            print("NoSuchElementException occurred..")
        self.lp.clicksignin()
        self.lp.userGreetingsbtn()
        self.lp.viewprofilebtn()
        self.lp.loginwithpasswordbtn()
        self.lp.setpassword(self.password)
        self.lp.loginwithpasswordbtn()
        time.sleep(1)
        act_title = self.driver.title
        # Verifying title of the login page using conditional statements
        if act_title == "Welcome to My IndiaMART":
            assert True
            print("This is title: ", act_title)
            self.logger.info('****Login test passed****')
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            act_title = self.driver.title
            print("This is title: ", act_title)
            self.lp.userGreetingsbtn()
            self.lp.clicksignout()
            self.driver.close()
            self.logger.error('****Login test failed****')
            assert False
