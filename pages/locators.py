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
    CART = (By.XPATH,
            "//div[@class='cart-wrapper']/div[@class='top-cart top-link-cart horizontal long-cart']/div[@class='block-title no-items  cart-button']/a[@class='cartHeader']/span[@class='title-cart clearfix']")
    PHONE_FIRST = (By.XPATH, "//a[@href='tel:+380500575097']")
    PHONE_SECOND = (By.XPATH, "//a[@href='tel:+380962174010']")
    PHONE_THIRD = (By.XPATH, "//a[@href='tel:+380931135146']")
    CALLBACK = (By.XPATH, "//a[@id='callback-button']")


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
    SLOTHOLDER_LEFT_ARROW = (By.XPATH, "//div[@class='tp-leftarrow tparrows default round hidearrows']")
    SLOTHOLDER_RIGHT_ARROW = (By.XPATH, "//div[@class='tp-rightarrow tparrows default round hidearrows']")
    MAGIC_ALPHABETS_CHRISTMAS_ALPHABET = (
        By.XPATH, "//div[@class='product-name']/a[@title='Чарівні абетки. Різдвяна абетка ']")
    FAIRY_ADVENTURES_OF_THE_FAIRY_AND_THE_DISAPPEARING_BRIDE = (
        By.XPATH, "//div[@class='product-name']/a[@title='Феєричні пригоди. Феї та зникла наречена ']")



