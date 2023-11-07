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
