from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Base():
    
    def __init__(self, browser):
        self.browser = browser
    
    def scroll_to_element(self, element):
        scroll_element = self.browser.find_element(By.XPATH, element)
        return ActionChains(self.browser).move_to_element(scroll_element)

    def scroll_home(self):
        return self.browser.execute_script("window.scrollTo(0, 0);")



    
        