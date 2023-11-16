import pytest
import random
from ..pages.base_page import BasePage  # дві крапки перед pages.base_page - абсолютний шлях до файлу
from ..pages.main_page import MainPage  # дві крапки перед settings - абсолютний шлях до файлу
from ..settings import sets  # дві крапки перед settings - абсолютний шлях до файлу


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        # pass
        hash_name = "%016x" % random.getrandbits(64)
        self.email_for_subscribe = f"{hash_name}@mail.com"

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

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_elem_fiction_literature()
        page.is_elem_children_literature()
        page.is_elem_popular_science_publicistics()
        page.is_elem_education()
        page.is_elem_business_literature()
        page.is_elem_medicine_health()
        page.is_elem_home_everydaylife_leisure()
        page.is_elem_spiritual_literature()
        page.is_elem_gift_editions()
        page.is_elem_stationery()
        page.is_elem_puzzle()
        page.is_elem_pictures_by_numbers()
        page.is_elem_slider_panel_first()
        page.is_elem_slider_panel_second()
        page.is_elem_slider_panel_third()
        page.is_elem_slider_panel_fourth()
        page.is_elem_slider_panel_fifth()
        page.is_elem_slider_panel_sixth()
        page.is_elem_slider_panel_seventh()
        page.is_elem_slider_panel_eighth()
        page.is_elem_slider_panel_ninth()
        page.is_elem_slotholder_left_arrow()
        page.is_elem_slotholder_right_arrow()
        page.is_elem_magic_alphabets_christmas_alphabet()
        page.is_elem_сeramic_hearts()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_elem_logo_footer()
        page.is_elem_input_subscribe()
        page.is_button_subscribe()

    def test_main_page_subscribe_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribe_action(self.email_for_subscribe)  # Передаємо згенерований імейл. див. рядок 16 цього файлу.
        # page.is_alert_success_after_subscribe() # В моєму сайті немає повідомлення про успішне підписання на розсилку новин

#########################################################################################################################
#                          EXAMPLES

# pytest
# pytest -s -v
# pytest -s -v tests/test_main_page.py
# pytest -s -v --browser_mode="gui"
# pytest -s -v -m "main_page"
#
# pytest -s -v {chrome, headless}
# pytest -s -v --browser_mode="gui" {chrome, gui}
# pytest -s -v --browser_name="firefox" {firefox, headless}
# pytest -s -v --browser_name="firefox" --browser_mode="gui"  {firefox, gui}
# pytest -s -v -m "main_page" --browser_mode="gui"
# pytest -s -v -m "main_page" --browser_name="firefox" --browser_mode="gui"
# pytest -s -v tests/test_main_page.py --browser_mode="gui"
# pytest -s -v tests/test_main_page.py --browser_name="firefox" --browser_mode="gui"
