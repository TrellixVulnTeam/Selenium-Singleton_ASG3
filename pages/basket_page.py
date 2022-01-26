from base.webapp import webapp


class BasketPage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BasketPage()
            return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def click_checkout(self):
        self.driver.find_element_by_id('checkout').click()
        return self


basket = BasketPage.get_instance()
