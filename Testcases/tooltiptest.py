from Utilities.Readproperties import readconfig
import pytest
from Pageobjects.ToolsQaPage import Toolstip


@pytest.mark.usefixtures("setup")
class test_tooltip:
    url = readconfig.getToolsqa_Url()

    @pytest.fixture(autouse=True)  # This fixture will act as support to setup driver
    def class_setup(self):
        self.ts = Toolstip(self.driver)  # This is to create one variable and use it widely for login page

    def test_001(self):
        self.driver.get(self.url)
        # print(self.driver.title)
        act_title = self.driver.title
        print(act_title)
