from selenium.webdriver.common.by import By

from Framework.pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def check_out_items(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
