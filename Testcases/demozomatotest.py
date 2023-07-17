import csv
import time
# import logging
# import pandas as pd
from selenium.webdriver.common.keys import Keys
import allure
import pytest
import xlsxwriter
from allure_commons.types import AttachmentType
from selenium.common.exceptions import InvalidElementStateException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pageobjects.ZomatoPage import zomato_main, zomato_product_page
from Utilities.Readproperties import readconfig
from Utilities.customLogger import configure_logger
from selenium import webdriver


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("setup")  # using pytest fixture to setup driver instances
class Test_Zomato_001:
    logger = configure_logger()

    # location = input("enter location name: ")

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.logger.info('****Initializing zomato_main page****')
        self.zo = zomato_main(self.driver)
        # self.mp = zomato_product_page(self.driver, )

    @allure.severity(allure.severity_level.MINOR)
    def test_zomato(self):
        # global data_list
        self.logger.info("********Opening Zomato URL*****")
        self.zo.url()
        self.logger.info("********Verifying page title*****")
        act_title = self.driver.title
        if self.driver.title == act_title:
            self.logger.info("********Page title is success*****")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Zomato_page_title",
                          attachment_type=AttachmentType.PNG)
            self.logger.info('****Page title is not matched****')
            assert False

        # self.zo.searchbox_location(self.location)
        # time.sleep(5)
        self.logger.info('****Getting all the mobile numbers from the businesses started****')
        self.logger.info('****filter has been selected****')
        self.zo.select_rating_filter()

        try:
            self.logger.info('****Initializing zomato_product_page****')
            self.mp = zomato_product_page(self.driver)
            # Wait for the list of products to be visible
            products = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, self.zo.select_foodstall)))
        except:
            pass
