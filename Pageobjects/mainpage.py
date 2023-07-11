from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys


class Mainpage:
    searchbox = "//input[@name='ss']"
    citybtn = "//span[text()='All India']"
    entercity = "//input[@placeholder='Enter city']"
    cityselect = "(//li[@class='as_D ui-menu-item'])[1]"
    contactNumbers = "//span[@class='pns_h duet fwb']"
    address = "//a[@class='clr3 fs12 fwn rsrc']"
    exporter = "//li//a[text()='Exporter']"
    Manufacturer = "//li//a[text()='Manufacturer']"
    Loadmore = "//div[@class='prd-shmr flx100 tac mt10 mb10']"
    SelectOnlyCity = "(//*[@class='clr8 ml5 flx1'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def search_box(self, itemname):
        ele = self.driver.find_element_by_xpath(self.searchbox)
        ele.clear()
        ele.send_keys(itemname)
        ele.send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath(self.searchbox).send_keys(itemname)
        # self.driver.find_element_by_xpath(self.searchbox).send_keys(Keys.ENTER)

    def city_btn(self):
        self.driver.find_element_by_xpath(self.citybtn).click()

    def enter_city(self, city):
        ele = self.driver.find_element_by_xpath(self.entercity)
        ele.clear()
        ele.send_keys(city)
        # self.driver.find_element_by_xpath(self.entercity).send_keys(Keys.ENTER)

    def city_select(self):
        self.driver.find_element_by_xpath(self.cityselect).click()

    def contact_num(self):
        self.driver.find_elements_by_xpath(self.contactNumbers)

    def addresses(self):
        self.driver.find_element_by_xpath(self.address)

    def click_exporter(self):
        self.driver.find_element_by_xpath(self.exporter).click()

    def click_Manufacturer(self):
        self.driver.find_element_by_xpath(self.Manufacturer).click()

    def load_more_results(self):
        self.driver.find_element_by_xpath(self.Loadmore)

    def Select_only_city(self):
        try:
            self.driver.find_element_by_xpath(self.SelectOnlyCity).click()
        except ElementNotInteractableException:
            print("ElementNotInteractableException is occured")
