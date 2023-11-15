from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):
    def is_link_login_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LINK_LOGIN_SIGNUP), \
            "The button 'link_login_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def click_link_login_signup(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LINK_LOGIN_SIGNUP), \
            "The button 'link_login_signup' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def click_button_signup(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_SIGNUP), \
            "The element 'button_signup' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_h3_zareiestruvatys(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H3_ZAREIESTRUVATYS), \
            "The element 'h3_zareiestruvatys' login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def input_firstname_lastname_email_password_signup(self, firstname, lastname, email, password):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_FIRSTNAME_SIGNUP, firstname), \
            "The element 'input_firstname_signup' is not inserted"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_LASTNAME_SIGNUP, lastname), \
            "The element 'input_lastname_signup' is not inserted"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_EMAIL_SIGNUP, email), \
            "The element 'input_email_signup' is not inserted"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD_SIGNUP, password), \
            "The element 'input_password_signup' is not inserted"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_CONFIRMATION_PASSWORD_SIGNUP, password), \
            "The element 'input_confirmation_password_signup' is not inserted"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def press_button_signup_submit(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_SIGNUP_SUBMIT), \
            "The element 'button_signup_submit' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success(self):
        assert self.is_element_appears_after_while(*locators.SignupLoginPageLocators.LOGIN_SIGNUP_SUCCESS, timeout=5), \
            "The element 'login_signup_success' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_my_account_in_header(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.MY_ACCOUNT), \
            "The button 'my_account' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def press_button_my_account(self):
        assert self.click_element(*locators.SignupLoginPageLocators.MY_ACCOUNT), \
            "The element 'my_account' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logout_in_header(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGOUT), \
            "Button 'logout' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def press_button_logout(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGOUT), \
            "The element 'logout' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_logout_success(self):
        assert self.is_element_appears_after_while(*locators.SignupLoginPageLocators.LOGOUT_SUCCESS, timeout=5), \
            "The element 'logout_success' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_h3_vkhid(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H3_VKHID), \
            "The element 'h3_vkhid' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def input_email_password_login(self, email, password):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_EMAIL_LOGIN, email), \
            "The element 'input_email_signup' is not inserted"
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD_LOGIN, password), \
            "The element 'input_password_signup' is not inserted"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def press_button_login_submit(self):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_LOGIN_SUBMIT), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")
