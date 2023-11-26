from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
import time
from base_class import Base

class MainPage(Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators

    button_smartphone = "//a[@data-meta-category='cardId-2']"
    button_sorting = "//button[2]/span[@class='e1b73xgd0 e106ikdt0 app-catalog-14yruy e1gjr6xo0']"
    min_price = "//div[2]/div/div[1]/input[1][@name='input-min']"
    max_price = "//div[2]/div/div[1]/input[2][@name='input-max']"
    rating_phone = "//input[@name='rating.4.5']"
    memori_phone = "//input[@id='23178_214256d1gb']"
    open_ram_phone = "//div[11]/div[1]/div/span[1][@class='app-catalog-277adr efrpyjy0']"
    ram_phone = "//input[@id='23177_2148d1gb']"
    open_type_display = "//div[14]/div[1]/div/span[1][@class='app-catalog-277adr efrpyjy0']"
    type_display = "//input[@id='9352_214oled']"
    open_screen_update = "//div[15]/div[1]/div/span[1][@class='app-catalog-277adr efrpyjy0']"
    screen_update = "//input[@id='14883_214120d1gts']"
    open_number_cores = "//div[24]/div[1]/div/span[1][@class='app-catalog-277adr efrpyjy0']"
    number_cores = "//input[@id='23412_2148']"
    open_volume_battery = "//div[30]/div[1]/div[1]/span[1][@class='app-catalog-277adr efrpyjy0']"
    volume_battery = "//input[@id='19462_214']"
    color_phone = "//input[@name='23179_214chernyy']"
    name_phone = "//div[3]/div[1]/a[@class='app-catalog-9gnskf e1259i3g0']"
    price_phone = "//span[@class='e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0']"
    phone_comparison = "//div[1]/div/div[4]/div/div[1]/button[@class='etd7ecp0 app-catalog-11xrwzj e8hswel0']"
    button_comparison = "//div[3]/div/a/div/div[@class='css-1wyvf5z eyoh4ac0']"
    mn_prc = "30000"
    mx_prc = "40000"

    # Getters

    def get_button_smartphone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_smartphone)))
    
    def get_button_sorting(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_sorting)))
    
    def get_min_price(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))
    
    def get_max_price(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_rating_phone(self):
        return self.browser.find_element(By.XPATH, self.rating_phone)
    
    def get_memori_phone(self):
        return self.browser.find_element(By.XPATH, self.memori_phone)

    def get_open_ram_phone(self):
        return self.browser.find_element(By.XPATH, self.open_ram_phone)

    def get_ram_phone(self):
        return self.browser.find_element(By.XPATH, self.ram_phone)
    
    def get_open_type_display(self):
        return self.browser.find_element(By.XPATH, self.open_type_display)

    def get_type_display(self):
        return self.browser.find_element(By.XPATH, self.type_display)
    
    def get_open_screen_update(self):
        return self.browser.find_element(By.XPATH, self.open_screen_update)

    def get_screen_update(self):
        return self.browser.find_element(By.XPATH, self.screen_update)

    def get_open_number_cores(self):
        return self.browser.find_element(By.XPATH, self.open_number_cores)

    def get_number_cores(self):
        return self.browser.find_element(By.XPATH, self.number_cores)

    def get_open_volume_battery(self):
        return self.browser.find_element(By.XPATH, self.open_volume_battery)

    def get_volume_battery(self):
        return self.browser.find_element(By.XPATH, self.volume_battery)

    def get_color_phone(self):
        return self.browser.find_element(By.XPATH, self.color_phone)
    
    def get_name_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_phone)))
    
    def get_price_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_phone)))
    
    def get_phone_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_comparison)))
    
    def get_button_comparison(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_comparison)))
    
    #  Actions

    def click_button_smartphone(self):
        self.get_button_smartphone().click()
        print("Click button smartphone")

    def click_button_sorting(self):
        time.sleep(2)
        self.get_button_sorting().click()
        print("Click button sorting")
    
    def input_min_price(self, mn_prc):
        time.sleep(2)
        self.get_min_price().clear()
        self.get_min_price().send_keys(mn_prc)
        print("Input min price")
    
    def input_max_price(self, mx_prc):
        time.sleep(2)
        self.get_max_price().clear()
        self.get_max_price().send_keys(mx_prc)
        self.get_min_price().click()
        print("Input max price")
    
    def click_rating_phone(self):
        self.scroll_to_element(self.rating_phone).click().perform()
        print("Scrolling and click rating phone")

    def click_memori_phone(self):
        time.sleep(2)
        self.scroll_to_element(self.memori_phone).click().perform()
        print("Scrolling and click memori phone")

    def click_ram_phone(self):
        time.sleep(2)
        self.scroll_to_element(self.open_ram_phone).click().perform()
        print("Scrolling and click open ram phone")
        self.scroll_to_element(self.ram_phone).click().perform()
        print("Scrolling and click ram phone")
        
    def click_display_type(self):
        time.sleep(2)
        self.scroll_to_element(self.open_type_display).click().perform()
        print("Scrolling and click open type display phone")
        self.scroll_to_element(self.type_display).click().perform()
        print("Scrolling and click type display phone") 

    def click_screen_update(self):
        time.sleep(2)
        self.scroll_to_element(self.open_screen_update).click().perform()
        print("Scrolling and click open screen update phone")
        self.scroll_to_element(self.screen_update).click().perform()
        print("Scrolling and click screen update phone")

    def click_number_cores(self):
        time.sleep(2)
        self.scroll_to_element(self.open_number_cores).click().perform()
        print("Scrolling and click open number cores phone")
        self.scroll_to_element(self.number_cores).click().perform()
        print("Scrolling and click number cores phone")

    def click_volume_battery(self):
        time.sleep(2)
        self.scroll_to_element(self.open_volume_battery).click().perform()
        print("Scrolling and click open battery phone")
        self.scroll_to_element(self.volume_battery).click().perform()
        print("Scrolling and click battery phone")

    def click_color_phone(self):
        time.sleep(2)
        self.scroll_to_element(self.color_phone).click().perform()
        print("Click black color")
        self.scroll_home()
        print("Scroll to home")

    def text_name_phone(self):
        time.sleep(2)
        print("Name phone: " + self.get_name_phone().text)

    def text_price_phone(self):
        time.sleep(2)
        print("Price phone: " + self.get_price_phone().text)

    def click_phone_comparison(self):
        time.sleep(2)
        self.get_phone_comparison().click()
        print("Click phone comparison")
    
    def click_button_comparison(self):
        time.sleep(2)
        self.get_button_comparison().click()
        print("Click button comparison")
    
    # Methods

    def selection_smartphone(self):
        self.click_button_smartphone()
        self.click_button_sorting()
        self.input_min_price(self.mn_prc)
        self.input_max_price(self.mx_prc)
        self.click_rating_phone()
        self.click_memori_phone()
        self.click_ram_phone()
        self.click_display_type()
        self.click_screen_update()
        self.click_number_cores()
        self.click_volume_battery()
        self.click_color_phone()
        self.text_name_phone()
        self.text_price_phone()
        self.click_phone_comparison()
        self.click_button_comparison()