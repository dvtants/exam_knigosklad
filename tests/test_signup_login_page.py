import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
# from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_logout
class TestSignupLoginLogautPage:

    def setup_method(self):
        hash_name = "%016x" % random.getrandbits(64)
        self.firstname_for_signup = "John"
        self.lasttname_for_signup = "Wick"
        self.email_for_signup = f"{hash_name}@mail.com"
        self.password_for_signup = "123654789"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()
        page.explicit_wait(2)

    def test_signup_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_link_login_signup()
        page.click_link_login_signup()
        page.explicit_wait(2)
        page.click_button_signup()
        page.explicit_wait(2)
        page.is_h3_zareiestruvatys()
        page.input_firstname_lastname_email_password_signup(self.firstname_for_signup, self.lasttname_for_signup,
                                                            self.email_for_signup, self.password_for_signup)
        page.explicit_wait(5)
        page.press_button_signup_submit()
        page.is_alert_success()
        page.explicit_wait(5)

    def test_logout_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_button_my_account_in_header()
        page.press_button_my_account()
        page.explicit_wait(2)
        page.is_button_logout_in_header()
        page.press_button_logout()
        # page = MainPage(browser, self.link_to_cabinet)
        # page.is_button_login()
        page.is_logout_success()
        page.explicit_wait(7)
        page.is_link_login_signup()

    def test_login_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_link_login_signup()
        page.click_link_login_signup()
        page.explicit_wait(2)
        page.is_h3_vkhid()
        page.input_email_password_login(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicit_wait(5)
        page.press_button_login_submit()
        page.is_alert_success()
        page.explicit_wait(5)
        page.press_button_my_account()
        page.press_button_logout()
        page.is_link_login_signup()

# pytest -s -v -m "signup_login_logout" --browser_mode="gui"
# pytest -s -v tests/test_signup_login_page.py --browser_mode="gui"
# pytest -s -v tests/test_signup_login_page.py --browser_name="firefox" --browser_mode="gui"
