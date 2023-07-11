from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class basedriver:

    def __init__(self, driver):
        self.driver = driver

    # Here we are creating custom method for webdriver wait
    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    #
    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element

    ###################### screenshot setup ########################

    def screenshot(self):
        self.driver.save_screenshot(".\\Screenshots\\" + "test_homePage_title.png")
