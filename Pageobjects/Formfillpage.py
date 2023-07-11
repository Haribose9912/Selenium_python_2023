import time
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from Utilities.base_driver import basedriver


class Formfill(basedriver):
    # locators of all webelements
    first_name = "//input[@name='first_name']"
    last_name = "//input[@name='last_name']"
    email = "//input[@name='email']"
    Phone_number = "//input[@name='phone']"
    address = "//input[@name='address']"
    city = "//input[@name='city']"
    state = "//select[@name='state']"  # select method used to work on dropdowns
    zip_code = "//input[@name='zip']"
    webiste = "//input[@name='website']"
    hosting_yes = "(//input[@name='hosting'])[1]"
    hosting_no = "(//input[@name='hosting'])[2]"
    description = "//textarea[@name='comment']"
    send_btn = "//*[text()='Send ']"
    formfill_url = "https://demo.seleniumeasy.com/input-form-demo.html"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Form_url(self):
        self.driver.get(self.formfill_url)

    def getfirstnameFiled(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.first_name)

    def eneter_firstname(self, fname):
        self.getfirstnameFiled().clear()
        self.getfirstnameFiled().send_keys(fname)
        self.getfirstnameFiled().send_keys(Keys.ENTER)

    def getlastnameFiled(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.last_name)

    def enter_lastname(self, lname):
        self.getlastnameFiled().clear()
        self.getlastnameFiled().send_keys(lname)
        self.getlastnameFiled().send_keys(Keys.ENTER)

    def getEmail_id(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.email)

    def enter_email_id(self, email_address):
        self.getEmail_id().clear()
        self.getEmail_id().send_keys(email_address)
        self.getEmail_id().send_keys(Keys.ENTER)

    def getPhone(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.Phone_number)

    def enter_PhoneNumber(self, phonenum):
        self.getPhone().clear()
        self.getPhone().send_keys(phonenum)
        self.getPhone().send_keys(Keys.ENTER)

    def getaddress(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.address)

    def enter_addresses(self, Address):
        self.getaddress().clear()
        self.getaddress().send_keys(Address)
        self.getaddress().send_keys(Keys.ENTER)

    def get_city(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.city)

    def enter_city(self, City):
        self.get_city().clear()
        self.get_city().send_keys(City)
        self.get_city().send_keys(Keys.ENTER)

    def get_state(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.state)

    # select method used to handle drop down
    def select_state(self):
        x = self.get_state()
        select = Select(x)
        select.select_by_visible_text("Indiana")
        time.sleep(2)

    def get_zipcode(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.zip_code)

    def enter_zipcode(self, zip):
        self.get_zipcode().clear()
        self.get_zipcode().send_keys(zip)
        self.get_zipcode().send_keys(Keys.ENTER)

    def get_website(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.webiste)

    def enter_website_info(self, Website):
        self.get_website().clear()
        self.get_website().send_keys(Website)
        self.get_website().send_keys(Keys.ENTER)

    def click_hosting_btn_yes(self):
        self.wait_until_element_is_clickable(By.XPATH, self.hosting_yes).click()

    def click_hosting_btn_no(self):
        self.wait_until_element_is_clickable(By.XPATH, self.hosting_no).click()

    def get_description(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.description)

    def enter_description_info(self, des_info):
        self.get_description().clear()
        self.get_description().send_keys(des_info)
        self.get_description().send_keys(Keys.ENTER)

    def click_sendButton(self):
        self.wait_until_element_is_clickable(By.XPATH, self.send_btn).click()

    def full_form_fill(self, fname, lname, email, phone, address, city, zipcode, website, description):
        self.eneter_firstname(fname)
        self.enter_lastname(lname)
        self.enter_email_id(email)
        self.enter_PhoneNumber(phone)
        self.enter_addresses(address)
        self.enter_city(city)
        self.select_state()
        self.enter_zipcode(zipcode)
        self.enter_website_info(website)
        self.click_hosting_btn_yes()
        self.enter_description_info(description)
        self.click_sendButton()
        fil_form = self.full_form_fill
        return fil_form
