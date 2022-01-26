from pages.login_page import login
from pages.home_page import home
from pages.basket_page import basket
from pages.checkout_info_page import checkout
from pages.checkout_overview_page import overview
from pages.checkout_complete import complete
from utils.sql_util import SQLUtil


class PurchaseFacade:
    def purchase_item(self, item):
        login.enter_credentials().click_login_button()
        home.verify_login().add_item_to_basket(item).open_basket()
        basket.click_checkout()
        checkout.enter_details()
        checkout.click_continue()
        overview.click_finish()
        complete.click_back_home()
        home.verify_login()

    def purchase_item_data_driven(self):
        items = SQLUtil.read_data(self, "name", "shopping_items")
        login.enter_credentials().click_login_button()

        for text in items:
            text_value = text[0]
            home.verify_login().add_item_to_basket(text_value).open_basket()
            basket.click_checkout()
            checkout.enter_details()
            checkout.click_continue()
            overview.click_finish()
            complete.click_back_home()
            home.verify_login()
            print(f'{text_value} purchase passed')