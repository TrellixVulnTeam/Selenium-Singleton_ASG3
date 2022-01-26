import time
import unittest
import pytest
from pages.home_page import home
from pages.login_page import login
from pages.home_page import home
from pages.basket_page import basket
from pages.checkout_info_page import checkout
from pages.checkout_overview_page import overview
from pages.checkout_complete import complete
from facade.purchase_facade import PurchaseFacade


@pytest.mark.usefixtures('setup')
class TestPurchases:
    def test_purchase_item_fluentPo(self):
        login.enter_credentials().click_login_button()
        home.verify_login().add_item_to_basket('Sauce Labs Backpack').open_basket()
        basket.click_checkout()
        checkout.enter_details()
        checkout.click_continue()
        overview.click_finish()
        complete.click_back_home()
        home.verify_login()

    def test_facade_purchase(self):
        PurchaseFacade.purchase_item(self, 'Sauce Labs Onesie')

    def test_data_driven_purchases(self):
        PurchaseFacade.purchase_item_data_driven(self)


if __name__ == '__main__':
    unittest.main()
