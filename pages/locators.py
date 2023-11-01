from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, "//img[@src='https://knigosklad.com.ua/media/logo_ks.png']")
    ABOUT_US = (By.XPATH, "//li[@class='level0 first ']")
    PAYMENT_DELIVERY = (By.XPATH, "//li[@class='level0 ']")
    CONTACTS = (By.XPATH, "//li[@class='level0 last ']")
    SEARCH = (By.XPATH, "//input[@id='search_287']")
    BUTTON_SUBMIT = (By.XPATH,
                     "//form[@id='search_mini_form_287']/div[@class='form-search']/div[@class='indent']/button[@class='btn btn-default']")
    CATALOG_GOODS = (By.XPATH, "//button[@class='menu-button-catalog-slide active']")
    LANGUAGE_UKR = (By.XPATH, "//li[@class='language-switcher__item']/span[text()='Укр']")
    LANGUAGE_RUS = (By.XPATH, "//li[@class='language-switcher__item']/a[text()='Рус']")
    ENTRANCE = (By.XPATH, "//ul[@class='links']")
    CART = (By.XPATH,
            "//div[@class='cart-wrapper']/div[@class='top-cart top-link-cart horizontal long-cart']/div[@class='block-title no-items  cart-button']/a[@class='cartHeader']/span[@class='title-cart clearfix']")
    PHONE_FIRST = (By.XPATH, "//a[@href='tel:+380500575097']")
    PHONE_SECOND = (By.XPATH, "//a[@href='tel:+380962174010']")
    PHONE_THIRD = (By.XPATH, "//a[@href='tel:+380931135146']")
    CALLBACK = (By.XPATH, "//a[@id='callback-button']")


