from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_class import Base
import time

class EntryPage(Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    name = "Максим"
    surname = "Пастухов"
    e_mail = "addressdecim@gmail.com"
    telephone = "89042804343"
    city = "Липецк"
    street = "проспект 60 лет СССР"
    house = "27"
    porch = "3"
    floor = "9"
    flat = "105"
    
    # Locators
    
    recipient_details = "//button[@class='e4uhfkv0 css-pjyyz3 e4mggex0']"
    inpt_name = "//input[@placeholder='Имя']"
    inpt_surname = "//input[@placeholder='Фамилия']"
    inpt_telephone = "//input[@placeholder='Телефон']"
    button_create = "//div[4]/button[@data-meta-name='RecipientForm__action-button']"
    button_delivery = "//label[@class='el7jmaq0 e1twwlg30 css-1ia32xb e1amf8g0']"
    inpt_city = "//input[@name='city']"
    inpt_street = "//input[@name='street']"
    clck_street = "//div[@class='e1i7snhg0 css-zb5ocs e17hwyhm0']"
    inpt_house = "//input[@name='courier-delivery-new-address-form_house']"
    inpt_porch = "//input[@name='courier-delivery-new-address-form_porch']"
    inpt_floor = "//input[@name='courier-delivery-new-address-form_floor']"
    inpt_flat = "//input[@name='courier-delivery-new-address-form_flat']"
    payment_method = "//label[2][@class='eddme6n0 e1twwlg30 css-1mlhsy e1amf8g0']"
    button_checkout = "//button[@data-meta-name='SubmitButton']"
    
    # Getters

    def get_recipient_details(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.recipient_details)))
    
    def get_input_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_name)))
    
    def get_input_surname(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_surname)))
    
    def get_input_telephone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_telephone)))
    
    def get_button_create(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_create)))
    
    def get_button_delivery(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_delivery)))
    
    def get_input_city(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_city)))
    
    def get_input_street(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_street)))
    
    def get_clck_street(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.clck_street)))

    def get_input_house(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_house)))
    
    def get_input_porch(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_porch)))
    
    def get_input_floor(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_floor)))
    
    def get_input_flat(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.inpt_flat)))
    
    def get_payment_method(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method)))
    
    def get_button_checkout(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))
    
    #  Actions

    def click_recipient_details(self):
        self.get_recipient_details().click()
        print("Click recipient details")
    
    def input_name(self, nm):
        self.get_input_name().send_keys(nm)
        print("input name")
    
    def input_surname(self, srnm):
        self.get_input_surname().send_keys(srnm)
        print("input surname")

    def input_telephone(self, tlphn):
        self.get_input_telephone().send_keys(tlphn)
        print("input telephone")

    def click_button_create(self):
        self.get_button_create().click()
        print("Click button create")
    
    def click_button_delivery(self):
        time.sleep(2)
        self.get_button_delivery().click()
        print("Click button delivery")

    def input_city(self, ct):
        self.get_input_city().send_keys(ct)
        print("Input city")
    
    def input_street(self, strt):
        self.get_input_street().send_keys(strt)
        self.get_clck_street().click
        print("Input street")
    
    def input_house(self, hs):
        self.get_input_house().send_keys(hs)
        print("Input house")
    
    def input_porch(self, prch):
        self.get_input_porch().send_keys(prch)
        print("Input porch")

    def input_floor(self, flr):
        self.get_input_floor().send_keys(flr)
        print("Input floor")

    def input_flat(self, flt):
        time.sleep(2)
        self.get_input_flat().send_keys(flt)
        print("Input flat")
    
    def click_payment_method(self):
        time.sleep(2)
        self.scroll_to_element(self.payment_method).click().perform()
        print("Scroll and click payment method")
    
    def scroll_button_checkout(self):
        time.sleep(2)
        self.scroll_to_element(self.button_checkout)
        time.sleep(2)
        print("Scroll to element")

    def filling(self):
        self.click_recipient_details()
        self.input_name(self.name)
        self.input_surname(self.surname)
        self.input_telephone(self.telephone)
        self.click_button_create()
        self.click_button_delivery()
        self.input_city(self.city)
        self.input_street(self.street)
        self.input_house(self.house)
        self.input_porch(self.porch)
        self.input_floor(self.floor)
        self.input_flat(self.flat)
        self.click_payment_method()
        self.scroll_button_checkout()