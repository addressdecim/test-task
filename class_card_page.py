from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_class import Base
import time

class CartPage(Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    
    name_phone_comparison = "//div[3]/div[2]/div[1]/a[@class='  Link js--Link Link_type_user-profile']"
    price_phone_comparison = "//div[1]/div[2]/span/span[1][@class='Compare__product-cell_price_current-price js--Compare__product-cell_price_current-price ']"
    type_display_comparison = "//div[10]/div[2]/div[2]/div/div[@class='Compare__specification-cell js--Compare__specification-cell']"
    screen_update_comparison = "//div[10]/div[18]/div[2]/div/div[@class='Compare__specification-cell js--Compare__specification-cell']"
    number_cores_comparison = "//div[12]/div[6]/div[2]/div/div[@class='Compare__specification-cell js--Compare__specification-cell']"
    ram_phone_comparison = "//div[12]/div[14]/div[2]/div/div[@class='Compare__specification-cell js--Compare__specification-cell']"
    memori_phone_comparison = "//div[12]/div[16]/div[2]/div/div[@class='Compare__specification-cell js--Compare__specification-cell']"
    button_add_cart = "//button[@data-label='В корзину']"
    button_go_cart = "//div[2]/button[@data-label='Перейти в корзину']"
    button_decor = "//button[@title='Перейти к оформлению']"
    total_name_phone = "//span[@class='e27li280 e106ikdt0 css-1qo2d1j e1gjr6xo0']"
    total_price_phone = "//span[@class='e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0']"
    
    # Getters

    def get_name_phone_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_phone_comparison)))
    
    def get_price_phone_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_phone_comparison)))
    
    def get_type_display_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_display_comparison)))

    def get_screen_update_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.screen_update_comparison)))
    
    def get_number_cores_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_cores_comparison)))
    
    def get_ram_phone_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.ram_phone_comparison)))
    
    def get_memori_phone_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.memori_phone_comparison)))

    def get_button_add_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_cart)))
    
    def get_button_go_cart(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_cart)))

    def get_button_decor(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_decor)))

    #  Actions

    def text_name_phone_comparison(self):
        assert self.get_name_phone_comparison().text == "Смартфон REALME 11 Pro+ 8/256Gb, RMX3741, черный"
        print("Phone names match ٩(◕‿◕)۶")
    
    def text_price_phone_comparison(self):
        assert self.get_price_phone_comparison().text == "38 570"
        print("Phone price match ٩(◕‿◕)۶")
    
    def text_type_display_comparison(self):
        self.scroll_to_element(self.type_display_comparison)
        print("Scrolling type display")
        time.sleep(2)
        assert self.get_type_display_comparison().text == "OLED FHD+"
        print("Type display match ٩(◕‿◕)۶")
    
    def text_screen_update_comparison(self):
        self.scroll_to_element(self.screen_update_comparison)
        print("Scrolling screen update")
        time.sleep(2)
        assert self.get_screen_update_comparison().text == "120 Гц"
        print("Screen update match ٩(◕‿◕)۶")

    def text_number_cores_comparison(self):
        self.scroll_to_element(self.number_cores_comparison)
        print("Scrolling number cores")
        time.sleep(2)
        assert self.get_number_cores_comparison().text == "8"
        print("Number cores match ٩(◕‿◕)۶")

    def text_ram_phone_comparison(self):
        self.scroll_to_element(self.ram_phone_comparison)
        print("Scrolling RAM phone")
        time.sleep(2)
        assert self.get_ram_phone_comparison().text == "8 ГБ"
        print("RAM phone match ٩(◕‿◕)۶")

    def text_memori_phone_comparison(self):
        self.scroll_to_element(self.memori_phone_comparison)
        print("Scrolling memori phone")
        time.sleep(2)
        assert self.get_memori_phone_comparison().text == "256 ГБ"
        print("Memori phone match ٩(◕‿◕)۶")
        self.scroll_home()
        print("Scroll to home")

    def click_button_add_cart(self):
        self.get_button_add_cart().click()
        print("Click button add cart")
    
    def click_button_go_cart(self):
        self.get_button_go_cart().click()
        print("Click button go cart")

    def click_button_decor(self):
        self.get_button_decor().click()
        print("Click button decor")

    # Methods
    
    def select_card(self):
        self.text_name_phone_comparison()
        self.text_price_phone_comparison()
        self.text_type_display_comparison()
        self.text_screen_update_comparison()
        self.text_number_cores_comparison()
        self.text_ram_phone_comparison()
        self.click_button_add_cart()
        self.click_button_go_cart()
        self.click_button_decor()
