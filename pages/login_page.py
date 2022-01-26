from base.webapp import webapp


class LoginPage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
            return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def enter_credentials(self):
        self.driver.find_element_by_id('user-name').send_keys('standard_user')
        self.driver.find_element_by_id('password').send_keys('secret_sauce')
        return self

    def click_login_button(self):
        self.driver.find_element_by_id('login-button').click()
        return self


login = LoginPage.get_instance()
