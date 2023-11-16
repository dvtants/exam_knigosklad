import pytest
# import random
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
# from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def setup_method(self):
        pass
        # hash_name = "%032x" % random.getrandbits(128)
        # self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_login_to_cabinet(self, browser):
        pass
        # self.link_to_cabinet = browser.current_url
        # page = SignupLoginPage(browser, self.link_to_cabinet)
        # page.click_link_login_signup()
        # page.explicit_wait(2)
        # page.input_email_password_login(sets.TEST_EMAIL, sets.PASSWORD)
        # page.press_button_login_submit()
        # page.is_alert_success()
        # page.is_button_logout_in_header()
        # page = OrderPage(browser, self.link_to_cabinet)
        # page.click_on_logo()
        # page.explicit_wait(2)

    def test_add_products_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.add_to_cart_first_product()
        page.explicit_wait(2)
        page.press_btn_continue_shop()
        page.explicit_wait(2)
        page.click_on_logo()
        page.explicit_wait(2)
        page.add_to_cart_second_product()
        page.explicit_wait(10)
        page.add_to_cart_third_product()
        page.explicit_wait(10)

    def test_placing_an_order(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.order_selected_products_entrance()
        page.explicit_wait(2)
        page.order_selected_products_buyer_data()
        page.explicit_wait(2)
        page.order_selected_products_delivery_data_cities()
        #page.explicit_wait(2)
        page.order_selected_products_delivery_data_dnipro()
        page.explicit_wait(2)
        page.order_selected_products_delivery_data_method()
        page.explicit_wait(2)
        page.order_selected_products_payment_data()
        page.explicit_wait(2)
        page.order_selected_products_finish()
        page.explicit_wait(2)

# pytest -s -v -m "order_page" --browser_mode="gui"
# pytest -s -v -m "order_page" --browser_mode="gui"
# pytest -s -v tests/test_order_page.py --browser_mode="gui"
# pytest -s -v tests/test_order_page.py --browser_name="firefox" --browser_mode="gui"
# pytest -s -v --browser_mode="gui"
# pytest -s -v --browser_name="firefox"
