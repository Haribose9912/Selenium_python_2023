
import time
import pytest
from selenium.common.exceptions import InvalidElementStateException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from Pageobjects.login_page_data_driven import home_page, login_page_ddt
# from Pageobjects.loginpage import Loginpage
from Utilities.Readproperties import readconfig
from Utilities.customLogger import loggen
from selenium import webdriver
from Utilities import excelUtils


@pytest.mark.usefixtures("setup")
class Test_002_Login:
    # baseURL = readconfig.getApplicationURL()
    path = ".//TestData/Logindata.xlsx"
    logger = loggen()

    @pytest.fixture(autouse=True)  # This fixture will act as support to setup driver
    def class_setup(self):
        self.lg = login_page_ddt(self.driver)
        self.hg = home_page(self.driver)

    def test_login_DDT(self):
        self.logger.info("**************Test_002_DDT_Login***************")
        self.logger.info('****Verifying login test****')

        try:
            self.lg.login_url()
            self.rows = excelUtils.getRowCount(self.path, 'Logintest')
            print("Number of rows in the sheet: ", self.rows)
            # list_status = []
            for r in range(2, self.rows + 1):
                self.lg.login_url()
                self.user = excelUtils.readData(self.path, 'Logintest', r, 1)
                self.password = excelUtils.readData(self.path, 'Logintest', r, 2)
                # self.Expected_result = excelUtils.readData(self.path, 'sheet1',r,3)
                self.lg.enter_username(self.user)
                time.sleep(1)
                self.lg.enter_password(self.password)
                time.sleep(1)
                self.lg.click_submit()
                time.sleep(2)
                act_title = "Logged In Successfully | Practice Test Automation"
                try:
                    if self.driver.title == act_title:
                        self.hg.login_success()
                        self.hg.log_out()
                        # print("Title of the page : ", self.driver.title)
                        # print("Logged out from the site...")
                        print("Login Pass with user credentials: ", "username: ", self.user, "password: ", self.password)
                        assert self.driver.title == act_title
                    else:
                        self.driver.save_screenshot(".\\Screenshots\\" + "test_excel_login_ddt_fail.png")
                        print("Login failed with Invalid user credentials: ","username: ", self.user, "password: ", self.password)
                        assert self.driver.title != act_title

                except(NoSuchElementException, AttributeError):
                    print("NoSuchElementException occurred")
        except TimeoutException:
            print("TimeoutException occurred")
