from ..pages import base_page, locators
# import re
import inspect


class OrderPage(base_page.BasePage):

    def click_on_logo(self):
        assert self.click_element(*locators.BasePageLocators.LOGO), \
            "The element 'logo' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def add_to_cart_first_product(self):
        assert self.hover_action(*locators.MainPageLocators.FICTION_LITERATURE), \
            "The element FICTION_LITERATURE is not present"
        assert self.click_element(*locators.OrderPageLocators.HISTORICAL_LITERATURE), \
            "The element HISTORICAL_LITERATURE is not present or intractable"
        assert self.click_element(*locators.OrderPageLocators.HISTORIC_NOVELS), \
            "The element HISTORIC_NOVELS is not present or intractable"
        assert self.click_element(*locators.OrderPageLocators.UKRAINIAN_LANGUAGE), \
            "The element UKRAINIAN_LANGUAGE is not present or intractable"
        assert self.click_element(*locators.OrderPageLocators.BUY_VOHNIANI_BRAMY), \
            "The element BUY_VOHNIANI_BRAMY is not present or intractable"
        assert self.is_element_present(*locators.OrderPageLocators.SUCCESSFULLY_ADDED_CART), \
            "The element 'SUCCESSFULLY_ADDED_CART' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def press_btn_continue_shop(self):
        assert self.click_element(*locators.OrderPageLocators.GO_TO_THE_STORE), \
            "The element cGO_TO_THE_STORE is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def add_to_cart_second_product(self):
        assert self.click_element(*locators.OrderPageLocators.BUY_RIZDVIANA_ABETKA), \
            "The element BUY_RIZDVIANA_ABETKA is not present or intractable"
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.SUCCESSFULLY_ADDED_CART_POPUP,
                                                   timeout=5), \
            "The element 'SUCCESSFULLY_ADDED_CART' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def add_to_cart_third_product(self):
        assert self.click_element(*locators.OrderPageLocators.BUY_PEREMAHATY), \
            "The element BUY_PEREMAHATY is not present or intractable"
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.SUCCESSFULLY_ADDED_CART_POPUP,
                                                   timeout=5), \
            "The element 'SUCCESSFULLY_ADDED_CART' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_entrance(self):
        assert self.hover_action(*locators.OrderPageLocators.CART_ITEMS_LOGO), \
            "The element 'CART_ITEMS' is not present"
        assert self.click_element(*locators.OrderPageLocators.CHECK_CART_LOGO), \
            "The element 'CHECK_CART' is not present or intractable"
        assert self.is_element_present(*locators.OrderPageLocators.TEXT_KOSHYK), \
            "The element 'KOSHYK' is not present"
        assert self.click_element(*locators.OrderPageLocators.BUTTON_ORDER_PRODUCTS), \
            "The element 'BUTTON_ORDER_PRODUCTS' is not present or intractable"
        assert self.is_element_present(*locators.OrderPageLocators.TEXT_ZAMOVLENNIA), \
            "The element 'ZAMOVLENNIA' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_buyer_data(self):
        assert self.is_element_present(*locators.OrderPageLocators.INPUT_FIRSTNAME_ORDER), \
            "The element 'INPUT_FIRSTNAME_ORDER' is not present"
        assert self.input_data(*locators.OrderPageLocators.INPUT_FIRSTNAME_ORDER, "BRED"), \
            "The element 'INPUT_FIRSTNAME_ORDER' is not inserted"
        self.explicit_wait(1)
        assert self.is_element_present(*locators.OrderPageLocators.INPUT_LASTNAME_ORDER), \
            "The element 'INPUT_LASTNAME_ORDER' is not present"
        assert self.input_data(*locators.OrderPageLocators.INPUT_LASTNAME_ORDER, "PITT"), \
            "The element 'INPUT_LASTNAME_ORDER' is not inserted"
        self.explicit_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_delivery_data_cities(self):
        assert self.is_element_present(*locators.OrderPageLocators.NOVAPOSHTA_CITIES_CHOSEN), \
            "The element 'NOVAPOSHTA_CITIES_CHOSEN' is not present"
        assert self.click_element(*locators.OrderPageLocators.NOVAPOSHTA_CITIES_CHOSEN), \
            "The element 'NOVAPOSHTA_CITIES_CHOSEN' is not intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_delivery_data_dnipro(self):
        assert self.is_element_present(*locators.OrderPageLocators.DNIPRO), \
            "The element 'DNIPRO' is not present"
        assert self.click_element(*locators.OrderPageLocators.DNIPRO), \
            "The element 'DNIPRO' is not intractable"
        self.explicit_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_delivery_data_method(self):
        assert self.is_element_present(*locators.OrderPageLocators.INPUT_DELIVERY_METHOD), \
            "The element 'INPUT_DELIVERY_METHOD' is not present"
        assert self.click_element(*locators.OrderPageLocators.INPUT_DELIVERY_METHOD), \
            "The element 'INPUT_DELIVERY_METHOD' is not intractable"
        self.explicit_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_payment_data(self):
        assert self.is_element_present(*locators.OrderPageLocators.INPUT_PAYMENT_ON_RECEIPT), \
            "The element 'INPUT_PAYMENT_ON_RECEIPT' is not present"
        assert self.click_element(*locators.OrderPageLocators.INPUT_PAYMENT_ON_RECEIPT), \
            "The element 'INPUT_PAYMENT_ON_RECEIPT' is not intractable"
        self.explicit_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def order_selected_products_finish(self):
        assert self.input_data(*locators.OrderPageLocators.NOTICE, "SORRY TEST"), \
            "The element 'NOTICE' is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.OrderPageLocators.ORDER_FINISH), \
            "The element 'ORDER_FINISH' is not present or intractable"
        assert self.input_data(*locators.OrderPageLocators.INPUT_PHONE_ORDER, "671234567"), \
            "The element 'INPUT_PHONE_ORDER' is not inserted"
        assert self.click_element(*locators.OrderPageLocators.ORDER_FINISH), \
            "The element 'ORDER_FINISH' is not present or intractable"
        self.explicit_wait(5)
        assert self.is_element_present(*locators.OrderPageLocators.YOUR_ORDER_HAS_BEEN_ACCEPTED), \
            "The element 'YOUR_ORDER_HAS_BEEN_ACCEPTED' is not present"
        self.explicit_wait(5)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

#########################################################################################################################
#                          EXAMPLES
#     def add_to_cart_first_product(self):
#         assert self.hover_action(*locators.OrderPageLocators.FIRST_PRODUCT), \
#             "The element is not present"
#         assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_FIRST_PRODUCT), \
#             "The element is not present or intractable"
#         price = self.get_text(*locators.OrderPageLocators.PRICE_FIRST_PRODUCT)
#         price = int(price.replace(' грн.', ''))  # 170
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#         if price:
#             return price
#
#     def press_btn_continue_shop_popup(self):
#         assert self.click_element(*locators.OrderPageLocators.BTN_CONTINUE_SHOP_POPUP), \
#             "The element currency is not present or intractable"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def add_to_cart_second_product(self):
#         assert self.click_element(*locators.MainPageLocators.BEST_SELLERS_SHOW_ALL), \
#             "The element currency is not present or intractable"
#         self.explicit_wait(2)
#         assert self.clear_field(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY), \
#             "The element currency is not present"
#         assert self.input_data(*locators.OrderPageLocators.SECOND_PRODUCT_INPUT_NUMBER_QTY, 2), \
#             "The element currency is not present"
#         price = self.get_text(*locators.OrderPageLocators.PRICE_SECOND_PRODUCT)
#         price = int(price.replace(' грн.', '')) * 2
#         assert self.click_element(*locators.OrderPageLocators.BUTTON_ADD_SECOND_PRODUCT), \
#             "The element currency is not present or intractable"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#         if price:
#             return price
#
#     def check_total_price_qty(self, price1, price2, qty):
#         total_price = self.get_text(*locators.OrderPageLocators.TOTAL_PRICE)
#         self.explicit_wait(2)
#         total_price = int(re.sub("[^0-9]", "", total_price))
#         print(f"total_prise int: {total_price}")
#         total_actual = price1 + price2
#         print(f"total_actual int: {total_actual}")
#         assert total_actual == total_price, \
#             "Total price doesn't match to actual"
#         qty_actual = int(self.get_text(*locators.OrderPageLocators.QTY))
#         assert qty_actual == qty, \
#             "QTY doesn't match to actual"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def press_btn_checkout_popup(self):
#         assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BTN_POPUP), \
#             "The element currency is not present or intractable"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def add_notice(self):
#         assert self.input_data(*locators.OrderPageLocators.INPUT_NOTE, "Test.."), \
#             "The element currency is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def press_green_btn_checkout(self):
#         assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BUTTON), \
#             "The element currency is not present or intractable"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
#
#     def is_alert_success(self):
#         assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
#             "The element is not present"
#         print(f"{inspect.currentframe().f_code.co_name} - Ok")
