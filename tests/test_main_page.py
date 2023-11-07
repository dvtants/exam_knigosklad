import pytest
from ..pages.base_page import BasePage  # дві крапки перед pages.base_page - абсолютний шлях до файлу
from ..pages.main_page import MainPage
from ..settings import sets  # дві крапки перед settings - абсолютний шлях до файлу


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_elem_logo()
        page.is_elem_about_us()
        page.is_elem_payment_delivery()
        page.is_elem_contacts()
        page.is_elem_search()
        page.is_but_button_submit()
        page.is_elem_catalog_goods()
        page.is_elem_language_ukr()
        page.is_elem_language_rus()
        page.is_but_entrance()
        page.is_but_cart()
        page.is_elem_phone_first()
        page.is_elem_phone_second()
        page.is_elem_phone_third()
        page.is_elem_callback()






        # page.is_button_feedback()
        # page.is_button_delivery()
        # page.is_button_warranty()
        # page.is_number_phone()
        # page.is_element_currency()
        # page.is_element_currency_uah()
        # page.is_element_currency_usd()
        # page.is_element_currency_eur()
        # page.is_element_logo()

    # def test_login_logout(self, browser):
    #    link_to_site = browser.current_url

# pytest
# pytest -s -v
# pytest -s -v tests/test_main_page.py
# pytest -s -v --browser_mode="gui"
