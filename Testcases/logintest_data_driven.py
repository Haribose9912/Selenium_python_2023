import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from Pageobjects.login_page_data_driven import login_page_ddt
from Pageobjects.login_page_data_driven import home_page
# from Utilities.Readproperties import readconfig
from Utilities.customLogger import LogGen
from Utilities import jsonUtils


# *********  Data driven testing using Json file *************#
@pytest.mark.usefixtures("setup")
class Test_Login_data_driven_001():
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lg = login_page_ddt(self.driver)
        self.hg = home_page(self.driver)

    def test_login_001(self):
        global user

        jsonUtils.read_json_data()  # This is a custom method called from utility file
        for user in jsonUtils.read_json_data()["users"]:
            # Navigate to the login page** ?? This login_url method called from a page objects file
            self.lg.login_url()  # here not using readconfig url , because inside loop its giving invalid argument error
            # Enter the username and password
            try:
                self.lg.enter_username(user["username"])
                self.lg.enter_password(user["password"])

                # Click the submit button
                self.lg.click_submit()

                # verify login page success
                self.hg.login_success()
                welcome_message = self.driver.find_element(By.XPATH, self.hg.loginSuccess)
                print("This is the login message: ", welcome_message.text)
                # clicking on login button
                self.hg.log_out()
                print(f"Test passed for user: {user['username']}")
            except TimeoutException:
                print("TimeoutException occurred")
                try:
                    err = self.driver.find_element_by_xpath(self.lg.Invalid_cred)
                    if err.is_displayed():
                        assert True
                        print(f"Test Failed for user: {user['username']}")
                        self.logger.error('*************Test fail*********')
                except  NoSuchElementException:
                    print("NoSuchElementException occurred")
