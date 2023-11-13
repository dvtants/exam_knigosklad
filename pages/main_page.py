from ..pages import base_page, locators
import inspect  # потрібен щоби написати прінт


class MainPage(base_page.BasePage):
    def is_elem_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element 'logo' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_about_us(self):
        assert self.is_element_present(*locators.BasePageLocators.ABOUT_US), \
            "The element 'about_us' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_payment_delivery(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT_DELIVERY), \
            "The element 'payment_delivery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_contacts(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS), \
            "The element 'contacts' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH), \
            "The element 'search' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_but_button_submit(self):
        assert self.is_element_present(*locators.BasePageLocators.BUTTON_SUBMIT), \
            "The button 'button_submit' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_catalog_goods(self):
        assert self.is_element_present(*locators.BasePageLocators.CATALOG_GOODS), \
            "The element 'catalog_goods' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_language_ukr(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_UKR), \
            "The element 'language_ukr' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_language_rus(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_RUS), \
            "The element 'language_rus' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_but_entrance(self):
        assert self.is_element_present(*locators.BasePageLocators.ENTRANCE), \
            "The button 'entrance' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_but_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "The button 'cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    # def is_but_cart_noitems(self):
    #     assert self.is_element_present(*locators.BasePageLocators.CART_NOITEMS), \
    #         "The button 'cart' is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")

    # def is_but_cart_items(self):
    #     assert self.is_element_present(*locators.BasePageLocators.CART_ITEMS), \
    #         "The button 'cart' is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_phone_first(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_FIRST), \
            "The element 'phone_first' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_phone_second(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_SECOND), \
            "The element 'phone_second' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_phone_third(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE_THIRD), \
            "The element 'phone_third' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_callback(self):
        assert self.is_element_present(*locators.BasePageLocators.CALLBACK), \
            "The element 'callback' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_fiction_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.FICTION_LITERATURE), \
            "The element 'fiction_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_children_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.CHILDREN_LITERATURE), \
            "The element 'children_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_popular_science_publicistics(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_SCIENCE_PUBLICISTICS), \
            "The element 'popular_science_publicistics' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_education(self):
        assert self.is_element_present(*locators.MainPageLocators.EDUCATION), \
            "The element 'education' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_business_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.BUSINESS_LITERATURE), \
            "The element 'business_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_medicine_health(self):
        assert self.is_element_present(*locators.MainPageLocators.MEDICINE_HEALTH), \
            "The element 'fiction_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_home_everydaylife_leisure(self):
        assert self.is_element_present(*locators.MainPageLocators.HOME_EVERYDAYLIFE_LEISURE), \
            "The element 'home_everydaylife_leisure' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_spiritual_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.SPIRITUAL_LITERATURE), \
            "The element 'spiritual_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_gift_editions(self):
        assert self.is_element_present(*locators.MainPageLocators.GIFT_EDITIONS), \
            "The element 'gift_editions' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_stationery(self):
        assert self.is_element_present(*locators.MainPageLocators.STATIONERY), \
            "The element 'stationery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_puzzle(self):
        assert self.is_element_present(*locators.MainPageLocators.PUZZLE), \
            "The element 'puzzle' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_pictures_by_numbers(self):
        assert self.is_element_present(*locators.MainPageLocators.PICTURES_BY_NUMBERS), \
            "The element 'fiction_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_slider_panel_first(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDER_PANEL_FIRST), \
            "The element 'slider_panel_first' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_slotholder_left_arrow(self):
        assert self.hover_action(*locators.MainPageLocators.SLIDER_PANEL_FIRST), \
            "The element 'slider_panel_first' is not present"
        assert self.is_element_present(*locators.MainPageLocators.SLOTHOLDER_LEFT_ARROW), \
            "The element 'slotholder_left_arrow' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    # def is_elem_slotholder_left_arrow(self):
    #     assert self.is_element_present(*locators.MainPageLocators.SLOTHOLDER_LEFT_ARROW), \
    #         "The element 'slotholder_left_arrow' is not present"
    #     print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_slotholder_right_arrow(self):
        assert self.is_element_present(*locators.MainPageLocators.SLOTHOLDER_RIGHT_ARROW), \
            "The element 'slotholder_right_arrow' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_magic_alphabets_christmas_alphabet(self):
        assert self.is_element_present(*locators.MainPageLocators.MAGIC_ALPHABETS_CHRISTMAS_ALPHABET), \
            "The element 'magic_alphabets_christmas_alphabet' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_elem_fairy_adventures_of_the_fairy_and_the_disappearing_bride(self):
        assert self.is_element_present(
            *locators.MainPageLocators.FAIRY_ADVENTURES_OF_THE_FAIRY_AND_THE_DISAPPEARING_BRIDE), \
            "The element 'fairy_adventures_of_the_fairy_and_the_disappearing_bride' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")





#     def is_button_feedback(self):
#         assert self.hover_action(*locators.BasePageLocators.DETAILS), \
#             "Element 'Детали сотрудничества' is not present"
#         assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
#             "Button feedback is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_button_delivery(self):
#         assert self.hover_action(*locators.BasePageLocators.DETAILS), \
#             "Element 'Детали сотрудничества' is not present"
#         assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
#             "Button delivery is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_button_warranty(self):
#         assert self.hover_action(*locators.BasePageLocators.DETAILS), \
#             "Element 'Детали сотрудничества' is not present"
#         assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
#             "Button warranty is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_number_phone(self):
#         assert self.is_element_present(*locators.BasePageLocators.PHONE), \
#             "Number phone is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_element_currency(self):
#         assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
#             "The element currency is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_element_currency_uah(self):
#         assert self.click_element(*locators.BasePageLocators.CURRENCY), \
#             "The element currency is not present or intractable"
#         assert self.is_element_present(*locators.BasePageLocators.CURRENCY_UAH), \
#             "The element currency_uah is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_element_currency_usd(self):
#         assert self.click_element(*locators.BasePageLocators.CURRENCY), \
#             "The element currency is not present or intractable"
#         assert self.is_element_present(*locators.BasePageLocators.CURRENCY_USD), \
#             "The element currency_usd is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_element_currency_eur(self):
#         assert self.click_element(*locators.BasePageLocators.CURRENCY), \
#             "The element currency is not present or intractable"
#         assert self.is_element_present(*locators.BasePageLocators.CURRENCY_EUR), \
#             "The element currency_eur is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_element_logo(self):
#         assert self.is_element_present(*locators.BasePageLocators.LOGO), \
#             "The element logo is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")

# def is_main_slider(self):
#     assert self.is_element_present(*locators.MainPageLocators.MAIN_SLIDER), \
#         "The element 'main_slider' is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_cat_zaryadki(self):
#     assert self.is_element_present(*locators.MainPageLocators.CAT_ZARYADKI), \
#         "The element 'cat_zaryadki' is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_main_subcat(self):
#     assert self.hover_action(*locators.MainPageLocators.CAT_ZARYADKI), \
#         "Element 'cat_zaryadki' is not present"
#     assert self.is_element_present(*locators.MainPageLocators.MAIN_SUBCAT), \
#         "Element 'main subcategory' is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_info_block_refund(self):
#     assert self.is_element_present(*locators.MainPageLocators.REFUND), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_info_block_delivery(self):
#     assert self.is_element_present(*locators.MainPageLocators.FREE_SHIPPING), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_info_block_otsrochka(self):
#     assert self.is_element_present(*locators.MainPageLocators.PAYMENT_DELAY), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_info_block_support(self):
#     assert self.is_element_present(*locators.MainPageLocators.TECHNICAL_SUPPORT), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_show_new_products(self):
#     assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_SHOW_ALL), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_show_prev_new_products(self):
#     assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_LEFT), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_show_next_new_products(self):
#     assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_RIGHT), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_section_new_products(self):
#     assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_PANEL), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_new_product_8(self):
#     assert self.is_element_present(*locators.MainPageLocators.NEW_ARRIVALS_SMARTEX_XIAOMI_REDMI_NOTE_5_A_PRIME), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_show_hits(self):
#     assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_SHOW_ALL), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_prev_hits(self):
#     assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_LEFT), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_next_hits(self):
#     assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_RIGHT), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_section_hits(self):
#     assert self.is_element_present(*locators.MainPageLocators.BEST_SELLERS_PANEL), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_prev_trends(self):
#     assert self.is_element_present(*locators.MainPageLocators.TRENDS_2023_PREVIOUS), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_next_trends(self):
#     assert self.is_element_present(*locators.MainPageLocators.TRENDS_2023_NEXT), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
# def is_button_subscribe(self):
#     assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
#         "The element subscribe is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - OK")
#
# def is_elem_footer_logo(self):
#     assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
#         "The element footer logo is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - OK")
#
# def subscribe_action(self, email):
#     assert self.input_data(*locators.BasePageLocators.INPUT_SUBSCRIBE, email), \
#         "The element is not inserted"
#     self.explicit_wait(5)
#     assert self.click_element(*locators.BasePageLocators.SUBSCRIBE), \
#         "The element currency is not present or intractable"
#     print(f"{inspect.currentframe().f_code.co_name} - OK")
#
# def is_alert_success_after_subscribe(self):
#     assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
#         "The element is not present"
#     print(f"{inspect.currentframe().f_code.co_name} - OK")
