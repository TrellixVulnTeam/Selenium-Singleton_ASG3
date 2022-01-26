from base.webapp import webapp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutInfo:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = CheckoutInfo()
            return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def enter_details(self):
        webapp.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'checkout_info')))
        self.driver.find_element_by_name('firstName').send_keys('test_first_name')
        self.driver.find_element_by_id('last-name').send_keys('test_last_name')
        self.driver.find_element_by_id('postal-code').send_keys('nw10 8ef')
        return self

    def click_continue(self):
        self.driver.find_element_by_id('continue').click()
        return self


checkout = CheckoutInfo.get_instance()
