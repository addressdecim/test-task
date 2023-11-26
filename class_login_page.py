from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_class import Base

class LoginPage(Base):
    
    url = "https://www.citilink.ru/"
    tlphn = "89042804343"
    psswrd = "Qwerty147852"

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


    # Locators
    
    button_authorization = "//span[@class='en3k2720 e106ikdt0 css-1rzz8dw e1gjr6xo0']"
    number = "//input[@name='login']"
    password = "//input[@name='pass']"
    button_enter = "//button[@class='e4uhfkv0 css-ajbuym e4mggex0']"
    button_agreement = "//button[@class='e4uhfkv0 css-1lxdbiq e4mggex0']"
    # Getters

    def get_button_authorization(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_authorization)))
    
    def get_number(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.number)))
    
    def get_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    
    def get_button_enter(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))
    
    def get_button_agreement(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_agreement)))
    
    #  Actions

    def click_button_authorization(self):
        self.get_button_authorization().click()
        print("Click button authorization")
    
    def input_number(self, tlphn):
        self.get_number().send_keys(tlphn)
        print("Input number")
    
    def input_password(self, psswrd):
        self.get_password().send_keys(psswrd)
        print("Input password")

    def click_button_enter(self):
        self.get_button_enter().click()
        print("Click button enter")
    
    def click_button_agreement(self):
        self.get_button_agreement().click()
        print("Click button agreement")

    # Methods
    
    def authorization(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.click_button_agreement()
        self.click_button_authorization()
        self.input_number(self.tlphn)
        self.input_password(self.psswrd)
        self.click_button_enter()


