from selenium.webdriver.common.keys import Keys


class Zomato:
    order_online = "//*[text()='Order Online']"
    search_box = "//*[@class='sc-hvvHee ldPnxs']"
    select_location = "//li//*[@class='sc-dCaJBF sc-cXHFlN jZWYCm']" #use findelements method
    select_filter1 = "//div[@class='sc-lmuQER kghnYZ']//*[text()='Rating: 4.0+']"
    select_filter2 = "//*[text()='Pure Veg']"
    select_foodstall = "//a[@class='sc-hZeNU cijfCJ']" #use findelements method
    select_overview = "//*[text()='Overview']"
    Call_number = "//p[@class='sc-1hez2tp-0 fanwIZ']"

    def __init__(self,driver):
        self.driver = driver
    def searchbox(self,location):
        ele = self.driver.find_element_by_xpath(self.searchbox)
        ele.clear()
        ele.send_keys(location)
        ele.send_keys(Keys.ENTER)














