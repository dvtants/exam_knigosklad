from ..pages import base_page, locators
import inspect  # потрібен щоби написати прінт


class MainPage(base_page.BasePage):
    def is_elem_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element 'logo' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_about_us(self):
        assert self.is_element_present(*locators.BasePageLocators.ABOUT_US), \
            "The element 'about_us' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_payment_delivery(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT_DELIVERY), \
            "The element 'payment_delivery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_contacts(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS), \
            "The element 'contacts' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH), \
            "The element 'search' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_but_button_submit(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_SUBMIT), \
            "The button 'button_submit' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_catalog_goods(self):
        assert self.is_element_present(*locators.BasePageLocators.CATALOG_GOODS), \
            "The element 'catalog_goods' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_language_ukr(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_UKR), \
            "The element 'language_ukr' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_language_rus(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_RUS), \
            "The element 'language_rus' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_but_entrance(self):
        assert self.is_element_present(*locators.BasePageLocators.ENTRANCE), \
            "The button 'entrance' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_but_cart(self):  # локатор спрацьовує в незалежності від наявності товарів в кошику
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "The button 'cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_phone_first(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_FIRST), \
            "The element 'phone_first' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_phone_second(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_SECOND), \
            "The element 'phone_second' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_phone_third(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_THIRD), \
            "The element 'phone_third' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_callback(self):
        assert self.is_element_present(*locators.BasePageLocators.CALLBACK), \
            "The element 'callback' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_fiction_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.FICTION_LITERATURE), \
            "The element 'fiction_literature' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_children_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.CHILDREN_LITERATURE), \
            "The element 'children_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_popular_science_publicistics(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_SCIENCE_PUBLICISTICS), \
            "The element 'popular_science_publicistics' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_education(self):
        assert self.is_element_present(*locators.MainPageLocators.EDUCATION), \
            "The element 'education' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_business_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.BUSINESS_LITERATURE), \
            "The element 'business_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_medicine_health(self):
        assert self.is_element_present(*locators.MainPageLocators.MEDICINE_HEALTH), \
            "The element 'fiction_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_home_everydaylife_leisure(self):
        assert self.is_element_present(*locators.MainPageLocators.HOME_EVERYDAYLIFE_LEISURE), \
            "The element 'home_everydaylife_leisure' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_spiritual_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.SPIRITUAL_LITERATURE), \
            "The element 'spiritual_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_gift_editions(self):
        assert self.is_element_present(*locators.MainPageLocators.GIFT_EDITIONS), \
            "The element 'gift_editions' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_stationery(self):
        assert self.is_element_present(*locators.MainPageLocators.STATIONERY), \
            "The element 'stationery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_puzzle(self):
        assert self.is_element_present(*locators.MainPageLocators.PUZZLE), \
            "The element 'puzzle' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_pictures_by_numbers(self):
        assert self.is_element_present(*locators.MainPageLocators.PICTURES_BY_NUMBERS), \
            "The element 'fiction_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_first(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_FIRST), \
            "The element 'slider_panel_first' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_second(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_SECOND), \
            "The element 'slider_panel_second' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_third(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_THIRD), \
            "The element 'slider_panel_third' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_fourth(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_FOURTH), \
            "The element 'slider_panel_fourth' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_fifth(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_FIFTH), \
            "The element 'slider_panel_fifth' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_sixth(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_SIXTH), \
            "The element 'slider_panel_sixth' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_seventh(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_SEVENTH), \
            "The element 'slider_panel_seventh' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_eighth(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_EIGHTH), \
            "The element 'slider_panel_eighth' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slider_panel_ninth(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_NINTH), \
            "The element 'slider_panel_ninth' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slotholder_left_arrow(self):
        assert self.hover_action(*locators.MainPageLocators.SLIDER_PANEL_FIRST), \
            "The element 'slider_panel_first' is not present"
        self.explicit_wait(5)
        assert self.is_element_present(*locators.MainPageLocators.SLOTHOLDER_LEFT_ARROW), \
            "The element 'slotholder_left_arrow' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_slotholder_right_arrow(self):
        assert self.hover_action(*locators.MainPageLocators.SLIDER_PANEL_FIRST), \
            "The element 'slider_panel_first' is not present"
        self.explicit_wait(5)
        assert self.is_element_present(*locators.MainPageLocators.SLOTHOLDER_RIGHT_ARROW), \
            "The element 'slotholder_right_arrow' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_magic_alphabets_christmas_alphabet(self):
        assert self.is_element_present(*locators.MainPageLocators.MAGIC_ALPHABETS_CHRISTMAS_ALPHABET), \
            "The element 'magic_alphabets_christmas_alphabet' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_сeramic_hearts(self):
        assert self.is_element_present(*locators.MainPageLocators.CERAMIC_HEARTS), \
            "The element 'сeramic_hearts' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_logo_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element 'logo_footer' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_input_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.INPUT_SUBSCRIBE), \
            "The element 'input_subscribe' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_SUBSCRIBE), \
            "The element 'button_subscribe' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.INPUT_SUBSCRIBE, email), \
            "The element 'input_subscribe' is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.BasePageLocators.BUTTON_SUBSCRIBE), \
            "The element 'button_subscribe' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    # def is_alert_success_after_subscribe(self): # В моєму сайті немає повідомлення про успішне підписання на розсилку новин
    #     assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
    #         "The element is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - OK")

#########################################################################################################################
#                          EXAMPLES
#     def is_button_feedback(self):
#         assert self.hover_action(*locators.BasePageLocators.DETAILS), \
#             "Element 'Детали сотрудничества' is not present"
#         assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
#             "Button feedback is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_element_currency_uah(self):
#         assert self.click_element(*locators.BasePageLocators.CURRENCY), \
#             "The element currency is not present or intractable"
#         assert self.is_element_present(*locators.BasePageLocators.CURRENCY_UAH), \
#             "The element currency_uah is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_button_subscribe(self):
#         assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
#             "The element subscribe is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - OK")
#
#     def subscribe_action(self, email):
#         assert self.input_data(*locators.BasePageLocators.INPUT_SUBSCRIBE, email), \
#             "The element is not inserted"
#         self.explicit_wait(5)
#         assert self.click_element(*locators.BasePageLocators.SUBSCRIBE), \
#             "The element currency is not present or intractable"
#         print(f"{inspect.currentframe().f_code.co_name} - OK")
#
#     def is_alert_success_after_subscribe(self):
#         assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
#             "The element is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - OK")
