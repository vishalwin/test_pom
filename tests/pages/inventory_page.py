from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

class Inventory_Page(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME,"product_sort_container")
    
    def __init__(self,driver):
        super().__init__(driver)
        
    def select_sort_option(self,visible_text):
        time.sleep(10)
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)
        time.sleep(10)
        
    