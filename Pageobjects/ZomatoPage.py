from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.base_driver import basedriver
import time


class zomato_main(basedriver):
    order_online = "//*[text()='Order Online']"
    search_box = "//input[@fdprocessedid='qubtj']"
    select_location = "//p[@class='sc-1hez2tp-0 sc-fUKxqW ijxkwf']"  # use findelements method
    select_filter1 = "//*[text()='Rating: 4.0+']"
    select_filter2 = "//*[text()='Pure Veg']"
    select_foodstall = "//a[@class='sc-hSmEHG htzHpa']"  # use findelements method
    select_overview = "//*[text()='Overview']"
    Call_number = "//p[@class='sc-1hez2tp-0 fanwIZ']"
    zomato_url = "https://www.zomato.com/hyderabad"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def url(self):
        self.driver.get(self.zomato_url)

    def searchbox_location(self, location):
        ele = self.driver.find_element(By.XPATH, self.search_box)
        ele.clear()
        ele.send_keys(location)
        ele.send_keys(Keys.ENTER)

    def selectLoction(self):
        self.driver.find_elements_by_xpath(self.select_location)

    def orderonlinebtn(self):
        self.wait_until_element_is_clickable(By.XPATH, self.order_online).click()

    def select_rating_filter(self):
        self.wait_until_element_is_visible(By.XPATH, self.select_filter1).click()

    def get_all_foodstalls(self):
        return self.wait_until_all_elements_located(By.XPATH, self.select_foodstall)


class zomato_product_page(zomato_main):
    business_name = "//h1[@class='sc-7kepeu-0 sc-iSDuPN fwzNdh']"
    business_address = "//a[@class='sc-clNaTc vNCcy']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_overview(self):
        self.wait_until_element_is_clickable(By.XPATH, self.select_overview).click()

    def get_call_number(self):
        self.driver.find_elements(By.XPATH, self.Call_number)
        # for n in number:
        # print("This is the Contact number: ", n.text)

    def get_business_name(self):
        name = self.wait_until_element_is_visible(By.XPATH, self.business_name)
        # print("This is the business name: ", name.text)

    def get_business_address(self):
        address = self.wait_until_element_is_visible(By.XPATH, self.business_address)
        print("Address: ", address.text)

    # def click_element_with_retry(self, locator, retry_count=3):
    #     for _ in range(retry_count):
    #         try:
    #             element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #             self.driver.execute_script("arguments[0].click();", element)
    #             break
    #         except StaleElementReferenceException:
    #             pass
    #     else:
    #         raise Exception("Element could not be clicked after multiple retries")
