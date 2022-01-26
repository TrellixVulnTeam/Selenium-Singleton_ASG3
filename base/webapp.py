import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
            return cls.instance

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path='C:/chromedriver.exe', options=options)
        self.wait = WebDriverWait(self.driver, 5)

    def get_driver(self):
        return self.driver

    def go_to_page(self):
        self.driver.get('https://www.saucedemo.com')

    def quit_driver(self):
        self.driver.close()
        self.driver.quit()


webapp = WebApp.get_instance()