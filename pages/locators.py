from selenium.webdriver.common.by import By


class BasePageLocators:  # Локатори елементів, які не змінюються. Все що в хедері і в футері.
    LOGO = (By.XPATH, "//img[@src='https://knigosklad.com.ua/media/logo_ks.png']")
    ABOUT_US = (By.XPATH, "//li[@class='level0 first ']")
    PAYMENT_DELIVERY = (By.XPATH, "//li[@class='level0 ']")
    CONTACTS = (By.XPATH, "//li[@class='level0 last ']")
    SEARCH = (By.XPATH, "//div[@class='search-wrapper']//input[@class='form-control']")
    BUTTON_SUBMIT = (By.XPATH, "//div[@class='search-wrapper']//button[@class='btn btn-default']")
    CATALOG_GOODS = (By.XPATH, "//button[@class='navbar-toggle collapsed catalog']")
    LANGUAGE_UKR = (By.XPATH, "//li[@class='language-switcher__item']/span[text()='Укр']")
    LANGUAGE_RUS = (By.XPATH, "//li[@class='language-switcher__item']/a[text()='Рус']")
    ENTRANCE = (By.XPATH, "//ul[@class='links']")
    CART = (By.XPATH, "//div[@class='cart-wrapper']//a[@class='top-cart-icon']/i[@class='fa fa-shopping-cart']")
    # CART_NOITEMS = (By.XPATH,
    # "//div[@class='cart-wrapper']/div[@class='top-cart top-link-cart horizontal long-cart']/div[@class='block-title no-items  cart-button']/a[@class='cartHeader']/span[@class='title-cart clearfix']")
    # CART_ITEMS = (By.XPATH,
    # "//div[@class='cart-wrapper']/div[@class='top-cart top-link-cart horizontal long-cart']/div[@class='block-title  cart-button']/a[@class='cartHeader']/span[@class='title-cart clearfix']")
    PHONE_FIRST = (By.XPATH, "//a[@href='tel:+380500575097']")
    PHONE_SECOND = (By.XPATH, "//a[@href='tel:+380962174010']")
    PHONE_THIRD = (By.XPATH, "//a[@href='tel:+380931135146']")
    CALLBACK = (By.XPATH, "//a[@id='callback-button']")
    LOGO_FOOTER = (By.XPATH, "//div[@class='footer-logo']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@class='form-control required-entry validate-email']")
    BUTTON_SUBSCRIBE = (By.XPATH, "//div[@class='row newsletter-fullsite']//button[@class='btn btn-default']")
    # ALERT_SUCCESS = (By.XPATH, "//a[@     ]") # В моєму сайті немає повідомлення про успішне підписання до розсилки
    # ALERT_ERROR = (By.XPATH, "//a[@     ]") # В моєму сайті немає повідомлення про успішне підписання до розсилки


class MainPageLocators:  # Локатори елементів, які змінюються. Все що є на головній сторінці.
    FICTION_LITERATURE = (
        By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja']")
    CHILDREN_LITERATURE = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/detskaja']")
    POPULAR_SCIENCE_PUBLICISTICS = (
        By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/nauchno-populjarnaja']")
    EDUCATION = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/obrazovanie']")
    BUSINESS_LITERATURE = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/delovaja']")
    MEDICINE_HEALTH = (
        By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/medicina-i-zdorov-e']")
    HOME_EVERYDAYLIFE_LEISURE = (
        By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/dom-byt-dosug']")
    SPIRITUAL_LITERATURE = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/duhovnaja']")
    GIFT_EDITIONS = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/gifts']")
    STATIONERY = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/stationery']")
    PUZZLE = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/pazly']")
    PICTURES_BY_NUMBERS = (
        By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/kartiny-po-nomeram']")
    SLIDER_PANEL_FIRST = (By.XPATH, "//li[@data-link='detskaja/hudozhestvennaja']")
    SLIDER_PANEL_SECOND = (By.XPATH, "//li[@data-link='obrazovanie/srednjaja-shkola/vneklassnoe-chtenie']")
    SLIDER_PANEL_THIRD = (By.XPATH, "//li[@data-link='gifts']")
    SLIDER_PANEL_FOURTH = (By.XPATH, "//li[@data-link='obrazovanie/inostrannye-jazyki']")
    SLIDER_PANEL_FIFTH = (By.XPATH, "//li[@data-link='/hudozhestvennaja']")
    SLIDER_PANEL_SIXTH = (By.XPATH, "//li[@data-link='delovaja']")
    SLIDER_PANEL_SEVENTH = (By.XPATH, "//li[@data-link='kartiny-po-nomeram']")
    SLIDER_PANEL_EIGHTH = (By.XPATH, "//li[@data-link='stationery']")
    SLIDER_PANEL_NINTH = (By.XPATH, "//li[@data-link='stationery/igrushki-sklad']")
    # SLOTHOLDER_LEFT_ARROW = (By.XPATH, "//div[@class='tp-leftarrow tparrows default round hidearrows']//div[@class='tp-arr-imgholder']")
    SLOTHOLDER_LEFT_ARROW = (
        By.XPATH, "//div[@class='row clearfix']//div[@class='tp-leftarrow tparrows default round']")
    # SLOTHOLDER_RIGHT_ARROW = (By.XPATH, "//div[@class='tp-rightarrow tparrows default round hidearrows']")
    SLOTHOLDER_RIGHT_ARROW = (
        By.XPATH, "//div[@class='row clearfix']//div[@class='tp-rightarrow tparrows default round']")
    MAGIC_ALPHABETS_CHRISTMAS_ALPHABET = (
        By.XPATH, "//div[@class='product-name']/a[@title='Чарівні абетки. Різдвяна абетка ']")
    CERAMIC_HEARTS = (
        By.XPATH,
        "//div[@id='home-slider-7212']//div[@class='owl-wrapper']//li[3]//div[@class='product-name']")


class SignupLoginPageLocators:  # 10.11.2013 Th HomeWork:
    # ICON_LOGIN_SIGNUP = (By.XPATH, "//i[@class='fa fa-user']")
    LINK_LOGIN_SIGNUP = (By.XPATH, "//a[@class='top-link-login AjaxKit-Singlton-Click']")
    CLOSE_POPUP_WINDOW_LOGIN_SIGNUP = (By.XPATH, "//div[@id='AddToCart-popup']//i[@class='fa fa-times']")
    H3_VKHID = (By.XPATH, "//h3[text()='Вхід']")
    # LABEL_EMAIL_LOGIN = (By.XPATH, "//div[@class='form-group']//label[@for='email']")
    INPUT_EMAIL_LOGIN = (By.XPATH, "//input[@name='login[username]']")
    # LABEL_PASSWORD_LOGIN = (By.XPATH, "//div[@class='form-group']//label[@for='pass']")
    INPUT_PASSWORD_LOGIN = (By.XPATH, "//input[@name='login[password]']")
    CHECKBOX_REMEMBER_ME_LOGIN = (By.XPATH, "//li[@id='remember-me-box-login']//input[@name='persistent_remember_me']")
    # LABEL_REMEMBER_ME_LOGIN = (By.XPATH, "//label[@for='remember_meJK0mDDr6Iv']")
    BUTTON_LOGIN_SUBMIT = (By.XPATH, "//button[@class='ajaxkit-login-submit-form btn btn-primary']")
    BUTTON_SIGNUP = (By.XPATH, "//a[text()='Зареєструватись']")
    H3_ZAREIESTRUVATYS = (By.XPATH, "//h3[text()='Зареєструватись']")
    # TEXT_PERSONAL_INFO_SIGNUP = (By.XPATH, "//h3[text()='Персональна інформація']")
    # LABEL_FIRSTNAME_SIGNUP = (By.XPATH, "//label[@for='firstname']")
    INPUT_FIRSTNAME_SIGNUP = (By.XPATH, "//input[@name='firstname']")
    # LABEL_LASTNAME_SIGNUP = (By.XPATH, "//label[@for='lastname']")
    INPUT_LASTNAME_SIGNUP = (By.XPATH, "//input[@name='lastname']")
    # LABEL_EMAIL_SIGNUP = (By.XPATH, "//form[@id='ajaxkit-register-form-validate']//label[@for='email_address']")
    INPUT_EMAIL_SIGNUP = (By.XPATH, "//input[@class='form-control validate-email required-entry']")
    # CHECKBOX_SUBSCRIBE_NEWSLETTER_SIGNUP = (By.XPATH, "//input[@name='is_subscribed']")
    # LABEL_SUBSCRIBE_NEWSLETTER_SIGNUP = (By.XPATH, "//label[@for='is_subscribed']")
    # TEXT_PASSWORD_SIGNUP = (By.XPATH, "//h3[text()='Пароль']")
    # LABEL_PASSWORD_SIGNUP = (By.XPATH, "//label[@for='password']")
    INPUT_PASSWORD_SIGNUP = (By.XPATH, "//input[@name='password']")
    # LABEL_CONFIRMATION_PASSWORD_SIGNUP = (By.XPATH, "//label[@for='confirmation']")
    INPUT_CONFIRMATION_PASSWORD_SIGNUP = (By.XPATH, "//input[@name='confirmation']")
    CHECKBOX_REMEMBER_ME_SIGNUP = (
        By.XPATH, "//form[@id='ajaxkit-register-form-validate']//input[@name='persistent_remember_me']")
    # LABEL_REMEMBER_ME_SIGNUP = (By.XPATH, "//form[@id='ajaxkit-register-form-validate']//label[@for='remember_meayJrBWE8PV']")
    BUTTON_SIGNUP_SUBMIT = (By.XPATH, "//button[@class='ajaxkit-login-submit-form btn btn-default']")
    LOGIN_SIGNUP_SUCCESS = (By.XPATH, "//div[@id='ajaxkit-popup-content']")
    MY_ACCOUNT = (By.XPATH, "//span[@class='user-icon']")
    LOGOUT = (By.XPATH, "//a[@href='https://knigosklad.com.ua/ua/customer/account/logout/']")
    LOGOUT_SUCCESS = (
        By.XPATH, "//p[text()='Ви успішно вийшли і за 5 секунд для вас відкриється головна сторінка сайту!']")


class OrderPageLocators:  # 10.11.2013 Th HomeWork:
    # FICTION_LITERATURE = (By.XPATH, "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja']")
    HISTORICAL_LITERATURE = (By.XPATH,
                             "//div[@class='row clearfix']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura']")
    HISTORIC_NOVELS = (By.XPATH,
                       "//li[@class='amshopby-cat amshopby-cat-level-1']//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura/istoricheskie-romany']")
    UKRAINIAN_LANGUAGE = (By.XPATH,
                          "//a[@href='https://knigosklad.com.ua/ua/hudozhestvennaja/istoricheskaja-literatura/istoricheskie-romany/ukrains_ka']")
    # VOHNIANI_BRAMY = (By.XPATH, "//a[text()='Вогняні брами ']")
    BUY_VOHNIANI_BRAMY = (By.XPATH, "//li[4]//button[@class='btn btn-default btn-cart']")
    SUCCESSFULLY_ADDED_CART = (By.XPATH, "//span[text()=' - успішно доданий до кошика!']")
    # BOOK_SUCCESSFULLY_ADDED_CART_POPUPADD = (By.XPATH, "//div[@class='popup-text success-msg']")
    # CART_BUTTON_POPUPADD = (By.XPATH, "//button[@class='rewrite-to-url btn btn-default ']")
    # ORDER_BUTTON_POPUPADD = (By.XPATH, "//div[@class='popup-added-product-list']//div[3]//button[@class='btn btn-primary']")
    GO_TO_THE_STORE = (By.XPATH, "//button[@class='btn btn-default btn-continue']")
    # ROZGIN = (By.XPATH, "//a[text()='Метью Шардлейк.Розгін']")
    # BUY_ROZGIN = (By.XPATH, '//button[@onclick="setLocation("https://knigosklad.com.ua/ua/checkout/cart/add/uenc/aHR0cHM6Ly9rbmlnb3NrbGFkLmNvbS51YS91YS9odWRvemhlc3R2ZW5uYWphL2lzdG9yaWNoZXNrYWphLWxpdGVyYXR1cmEvaXN0b3JpY2hlc2tpZS1yb21hbnkvdWtyYWluc19rYT9pc19hamF4PTE,/product/80337/form_key/pg1QpZAv9cM5IJ7z/")"]')
    BUY_PEREMAHATY = (
        By.XPATH,
        "//div[@id='home-slider-7212']//li[2]//button[@class='btn btn-default btn-cart AjaxKit-addtocart-link']")
    SUCCESSFULLY_ADDED_CART_POPUP = (By.XPATH, "//div[@class='popup-text success-msg']")
    BUY_RIZDVIANA_ABETKA = (By.XPATH,
                            "//div[@id='home-slider-1326']//li[3]//button[@class='btn btn-default btn-cart AjaxKit-addtocart-link']")
    CART_ITEMS_LOGO = (By.XPATH,
                       "//div[@class='cart-wrapper']/div[@class='top-cart top-link-cart horizontal long-cart']/div[@class='block-title  cart-button']/a[@class='cartHeader']/span[@class='title-cart clearfix']")
    CHECK_CART_LOGO = (
        By.XPATH, "//div[@class='block block-content topCartContent active']//a[@class='view-full-cart']")
    ORDER_CART_ITEMS_LOGO = (
        By.XPATH, "//div[@class='block block-content topCartContent active']//button[@class='btn btn-primary']")
    TEXT_KOSHYK = (By.XPATH, "//h1[text()='Кошик']")
    TEXT_ZAMOVLENNIA = (By.XPATH, "//h1[text()='Замовлення']")
    BUTTON_ORDER_PRODUCTS = (By.XPATH, "//button[@class='btn btn-primary btn-proceed-checkout']")
    # LABEL_FIRSTNAME_ORDER = (By.XPATH, "//label[@for='billing:firstname']")
    INPUT_FIRSTNAME_ORDER = (By.XPATH, "//input[@name='billing[firstname]']")
    # LABEL_LASTNAME_ORDER = (By.XPATH, "//label[@for='billing:lastname']")
    INPUT_LASTNAME_ORDER = (By.XPATH, "//input[@name='billing[lastname]']")
    # LABEL_EMAIL_ORDER = (By.XPATH, "//label[@for='billing:email']")
    INPUT_EMAIL_ORDER = (By.XPATH, "//input[@name='billing[email]']")
    # LABEL_PHONE_ORDER = (By.XPATH, "//label[@for='billing:telephone']")
    INPUT_PHONE_ORDER = (By.XPATH, "//input[@name='billing[telephone]']")
    # TEXT_CHOOSE_CITY = (By.XPATH, "//div[text()='Виберіть місто']")
    NOVAPOSHTA_CITIES_CHOSEN = (
        By.XPATH, "//div[@id='novaposhta_cities_chosen']")
    # DNIPRO = (By.XPATH, "//li[@data-option-array-index='1']")
    DNIPRO = (By.XPATH, "//ul[@class='chosen-results']/li[@data-option-array-index='1']")
    # //button[@class="button btn btn-default"]
    # LABEL_DELIVERY_METHOD_PICK_UP_FROM_THE_STORE = (By.XPATH, "//label[@for='s_method_sy_novaposhta_type_WarehouseWarehouse']")
    INPUT_DELIVERY_METHOD = (By.XPATH, "//input[@id='s_method_freeshipping_freeshipping']")
    # INPUT_DELIVERY_METHOD = (By.XPATH, "//label[@for='s_method_freeshipping_freeshipping']")
    # INPUT_DELIVERY_METHOD = (By.XPATH, "//dd[@style='display: block;']//label[@for='s_method_freeshipping_freeshipping']")
    # LABEL_PAYMENT_ON_RECEIPT = (By.XPATH, "//label[@for='p_method_checkmo']")
    INPUT_PAYMENT_ON_RECEIPT = (By.XPATH, "//input[@id='p_method_checkmo']")
    NOTICE = (By.XPATH, "//textarea[@id='customer_comment']")
    ORDER_FINISH = (By.XPATH, "//button[@class='btn btn-primary btn-checkout opc-btn-checkout']")
    YOUR_ORDER_HAS_BEEN_ACCEPTED = (By.XPATH, "//h1[text()='Ваше замовлення прийнято.']")


class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass


class ProductPageLocators:
    pass

# Заморозка в консолі Хрому: setTimeout(function(){debugger;}, 5000)
