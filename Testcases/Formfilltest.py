import time
import pytest
from selenium import webdriver
from Utilities.customLogger import configure_logger
from Pageobjects.Formfillpage import Formfill
# from ddt import ddt, data, file_data, unpack
from Utilities.base_driver import basedriver


@pytest.mark.usefixtures("setup")
class Test_form_001:
    logger = configure_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.ff = Formfill(self.driver)
        self.ff.Form_url()

    def test_page_title(self):
        self.logger.info('****Verifying home page title****')

        act_title = self.driver.title
        exp_title = act_title
        if act_title == exp_title:
            print("Page title is matching")
            self.logger.info('****Home page titile passed****')
            self.driver.close()
            assert True
        else:
            print("Page title is not matching")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homePage_title.png")
            basedriver.screenshot()
            self.logger.warn('******Home page title is failed********')
            self.driver.close()
            assert False

    def test_form_fill(self):

        self.ff.full_form_fill("hariesh", "kumar", "hari@gmail.com", "040-9944996", "plot.no.94/p,subashnagar",
                               "hyderabad", "50055", "www.google.com", "testingworldnewapproach")
        time.sleep(2)

    def test_form_fill2(self):
        self.ff.full_form_fill("ravana", "kumara", "ravana@gmail.com", "040-9944996", "plot.no.94/p,subashnagar",
                               "malesiya", "50055", "www.ravana.com", "testingworldnewapproach")
        time.sleep(5)
