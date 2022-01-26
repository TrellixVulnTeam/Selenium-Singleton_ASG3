import time

import pytest
from selenium import webdriver
from base.webapp import webapp


@pytest.fixture()
def setup(request):
    webapp.go_to_page()
    yield
    webapp.quit_driver()