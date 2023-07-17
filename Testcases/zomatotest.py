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

            # Iterate through the list of products and click each one using JavaScriptExecutor
            # for product in range(len(products)):
            # for product in products:
            i = 0
            while i < len(products):
                try:

                    product = products[i]
                    # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                    i += 1
                    self.logger.info('****Scrolling to business****')
                    try:
                        for k in range(1):
                            actions = ActionChains(self.driver)
                            actions.move_to_element(product)
                            actions.perform()
                            # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                    except:
                        pass

                    self.logger.info('****clicking on business****')

                    self.driver.execute_script("arguments[0].click();", product)
                    self.logger.info('****clicking on overview****')
                    self.mp.click_overview()
                    self.logger.info('****Capturing business name****')
                    # self.mp.get_business_name()
                    self.logger.info('****Capturing business address****')
                    # self.mp.get_business_address()
                    self.logger.info('****Capturing mobile numbers from call element****')
                    # self.mp.get_call_number()

                    a = []
                    ele = self.driver.find_element(By.XPATH, self.mp.business_name)
                    a.append(ele.text)
                    b = []
                    for ele in self.driver.find_elements(By.XPATH, self.zo.Call_number):
                        b.append(ele.text)
                    c = []
                    ele = self.driver.find_element(By.XPATH, self.mp.business_address)
                    c.append(ele.text)

                    data_zip = zip(a, b, c)
                    data_list = list(data_zip)
                    # print(data_list)
                    data_str = ''.join(map(str, data_list))
                    print(data_str)

                    # Go back to the previous page to repeat the process with the next business
                    self.logger.info('****Navigating page back****')
                    self.driver.back()
                    # time.sleep(5)
                    self.logger.info('****Navigating page back****')
                    self.driver.back()
                    # time.sleep(5)

                except (StaleElementReferenceException, IndexError):
                    # self.logger.info('****Handling stale element exception and retrying****')
                    # If the element becomes stale, re-fetch the products and try clicking again

                    products = self.driver.find_elements(By.XPATH, self.zo.select_foodstall)
                    try:
                        # action_chains.send_keys(Keys.SPACE).perform()
                        product = products[i]
                        i += 1
                        # WebDriverWait(self.driver, 10).until(
                        #     EC.visibility_of_all_elements_located((By.XPATH, self.zo.select_foodstall)))
                        # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                        self.driver.find_element(By.XPATH, self.zo.select_foodstall).send_keys(Keys.ARROW_DOWN)
                        try:
                            # here writing loop to scroll to element for 2 times
                            for k in range(1):
                                actions = ActionChains(self.driver)
                                actions.move_to_element(product)
                                actions.perform()

                            # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                        except IndexError:
                            pass
                    except (StaleElementReferenceException, IndexError):
                        print("StaleElementReferenceException occurred")
                        pass

        finally:
            # Close the browser at the end
            self.logger.info('****closing the browser****')
            self.driver.close()
