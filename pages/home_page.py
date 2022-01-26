from base.webapp import webapp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = HomePage()
            return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def verify_login(self):
        self.driver.find_element_by_class_name('app_logo')
        webapp.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'app_logo')))
        return self

    def add_item_to_basket(self, el):
        item = el.lower().split(' ')
        new_item = '-'.join(item)
        self.driver.find_element_by_id(f'add-to-cart-{new_item}').click()
        return self

    def open_basket(self):
        self.driver.find_element_by_id('shopping_cart_container').click()
        return self


home = HomePage.get_instance()
