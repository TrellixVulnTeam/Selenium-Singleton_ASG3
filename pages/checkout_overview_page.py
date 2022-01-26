from base.webapp import webapp


class OverviewPage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = OverviewPage()
            return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def click_finish(self):
        self.driver.find_element_by_id('finish').click()
        return self


overview = OverviewPage.get_instance()