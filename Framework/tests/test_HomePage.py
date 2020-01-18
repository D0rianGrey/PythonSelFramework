import pytest

from Framework.TestData.HomePageData import HomePageData
from Framework.pageObjects.HomePage import HomePage
from Framework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        log.info("first name is " + get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["lastname"])
        homepage.get_check_box().click()
        self.selectOptionByText(homepage.get_gender(), get_data["gender"])

        homepage.submit_form().click()

        alert_text = homepage.get_success_message().text

        assert ("Success" in alert_text)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
