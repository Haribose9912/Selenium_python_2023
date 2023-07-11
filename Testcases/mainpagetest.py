import time

import pytest
import xlsxwriter
import csv
from selenium.common.exceptions import (
    StaleElementReferenceException,
    NoSuchElementException,
    TimeoutException,
    NoSuchWindowException,
)
from selenium.webdriver.common.by import By
from Pageobjects.mainpage import Mainpage
from Pageobjects.loginpage import Loginpage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Readproperties import readconfig


@pytest.mark.usefixtures("setup")  # using pytest fixture to setup driver instances
class Test001_Mainpage:
    baseURL = readconfig.getApplicationURL()
    mobilenumber = readconfig.getmobilenumber()
    password = readconfig.getpassword()
    # city = input("Enter City: ")
    city = "jaipur"
    # itemname = input("Enter Product: ")
    itemname = "Jeera"

    @pytest.fixture(autouse=True)  # This fixture will act as support to setup driver
    def class_setup(self):
        self.lp = Loginpage(self.driver)  # This is to create one variable and use it widely for login page

    def test_Search_Item(self):
        self.driver.get(self.baseURL)
        self.lp.setmobilenumber(self.mobilenumber)
        self.lp.clicksignin()
        self.lp.userGreetingsbtn()
        self.lp.viewprofilebtn()
        self.lp.loginwithpasswordbtn()
        self.lp.setpassword(self.password)
        self.lp.loginwithpasswordbtn()
        time.sleep(1)
        act_title = self.driver.title
        if act_title == "Welcome to My IndiaMART":
            assert True
            print("This is title: ", act_title)
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            act_title = self.driver.title
            print("This is title: ", act_title)
            assert False
        self.mp = Mainpage(
            self.driver
        )  # This is to create one variable and use it widely for Main page
        self.mp.city_btn()
        self.mp.enter_city(self.city)
        self.mp.city_select()
        self.mp.search_box(self.itemname)
        time.sleep(3)
        self.mp.Select_only_city()
        # self.mp.click_Manufacturer()
        # time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        try:
            loadmore = self.driver.find_element_by_xpath(self.mp.Loadmore)
        except NoSuchElementException:
            print("NoSuchElementException occurred..")

        try:
            showresults_wait = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div//span[text()=' Show More Results ']")
                )
            )
        except TimeoutException:
            print("TimeoutException occurred..")
        actions = ActionChains(self.driver)

        try:
            actions.move_to_element(showresults_wait)
            actions.perform()
        except UnboundLocalError:
            print("UnboundLocalError occurred..")
        time.sleep(5)

        for i in range(25):
            try:
                if loadmore.is_displayed():
                    assert True
                    # clicking on show more results button using Javascript executer and handling stale element
                    # exception using try and except
                    self.driver.execute_script(
                        "arguments[0].click();", showresults_wait
                    )
                    time.sleep(5)
                else:
                    print("All Numbers detection has been completed")
            except StaleElementReferenceException:
                print("StaleElementReferenceException occurred.")
            except NoSuchElementException:
                print("NoSuchElementException occurred.")
            except UnboundLocalError:
                print("UnboundLocalError occurred..")

        # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        # time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        try:
            a = []
            for element in self.driver.find_elements_by_xpath(self.mp.contactNumbers):
                # myFile.write(element.text + "\n")
                a.append(element.text)
            b = []
            for ele in self.driver.find_elements_by_xpath(self.mp.address):
                b.append(ele.text)
        except NoSuchWindowException:
            print("NoSuchWindowException occured")

        data_dict = dict(zip(b, a))  # Combiling two lists into dictionary
        # Write adderess and numbers to text file
        with open("Utilities/Output files/Numbers.txt", "w") as f:
            f.truncate(0)
            f.write(self.itemname + "\n")
            f.write("\n")
            f.write(self.city + "\n")
            for key, value in data_dict.items():
                f.write("%s : %s\n" % (key, value))
                f.write("\n")
        time.sleep(5)

        # Writing data to excel sheet using xlsxwriter
        workbook = xlsxwriter.Workbook("Utilities/Output files/output.xlsx")
        # Adding worksheet with specific name
        if len(self.itemname) < 20:
            worksheet = workbook.add_worksheet("IndiaMart " + self.itemname)
        else:
            worksheet = workbook.add_worksheet("IndiaMart")

        # Some data we want to write to the worksheet.
        data_list = list(zip(b, a))
        # Start from the first cell. Rows and
        # columns are zero indexed.
        row = 1
        col = 0
        # adding image to excel sheet
        worksheet.insert_image(
            "D3", "Utilities/Images/jatayu logo.png", {"x_offset": 2, "y_offset": 2}
        )
        # Add_format to method in workbook to make Heading text formatting and Highlighting
        cell_format = workbook.add_format()
        cell_format.set_bold()
        cell_format.set_font_color("Green")
        cell_format.set_font_size(16)
        cell_format.set_font_name("Times New Roman")
        # Column names writing like Headers
        worksheet.write("A1", "Business Name", cell_format)
        worksheet.write("B1", "Contact  Numbers", cell_format)
        # Iterate over the data and write it out row by row.
        for Address, number in data_list:
            worksheet.write(row, col, Address)
            worksheet.write(row, col + 1, number)
            row += 1
        worksheet.autofit()  # This is used to Fit text in the columns and rows
        worksheet.set_paper(9)  # To set page A4
        workbook.close()
        time.sleep(5)
        self.driver.close()
