from selenium import webdriver
from class_login_page import LoginPage
from class_main_page import MainPage
from class_card_page import CartPage
from class_entry_page import EntryPage

def test_select_product():
    browser = webdriver.Chrome()
    authorization = LoginPage(browser)
    authorization.authorization()
    select_phone = MainPage(browser)
    select_phone.selection_smartphone()
    cart = CartPage(browser)
    cart.select_card()
    data_input = EntryPage(browser)
    data_input.filling()
    print("Конец ! \(★ω★)/")

    