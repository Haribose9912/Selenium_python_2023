import pytest
import requests
from requests.exceptions import InvalidSchema, MissingSchema
from selenium.webdriver.common.by import By
from Pageobjects import login_page_data_driven
from Pageobjects.login_page_data_driven import login_page_ddt, home_page
from Utilities.customLogger import configure_logger


@pytest.mark.usefixtures("setup")
class Test_Brokenlinks():
    logger = configure_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lg = login_page_ddt(self.driver)
        self.hg = home_page(self.driver)

    def test_Broken_links(self):
        self.logger.info("google site has been opened")
        self.driver.get("https://www.google.com")
        links = self.driver.find_elements(By.TAG_NAME, "a")
        images = self.driver.find_elements(By.TAG_NAME, "img")
        print("No.of Links present in site are: ", len(links))
        print("No.of Images present in site are: ", len(images))
        try:
            # verifying broken links and status codes
            for link in links:
                url = link.get_attribute('href')
                result = requests.head(url)
                if result.status_code != 200:
                    print(url, result.status_code)

            # verifying broken images and status codes
            for img in images:
                r2 = requests.head(img.get_attribute('src'))
                print("Images validation....")
                if r2.status_code != 200:
                    print(img.get_attribute('src'), r2.status_code)
        except (InvalidSchema, MissingSchema):
            print("InvalidSchema occurred...")
