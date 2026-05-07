from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

class Inventory_Page(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME,"product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    
    def __init__(self,driver):
        super().__init__(driver)
        
    def select_sort_option(self, visible_text):
        time.sleep(10)
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)
        time.sleep(10)
    
    def get_product_names(self):
        """Get list of product names from the page"""
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [item.text for item in product_elements]
    
    def get_product_prices(self):
        """Get list of product prices from the page"""
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        prices = [float(item.text.replace("$", "")) for item in price_elements]
        return prices
    
    def verify_products_sorted_by_name_ascending(self):
        """Verify products are sorted A to Z"""
        names = self.get_product_names()
        assert names == sorted(names), f"Products are not sorted A to Z. Got: {names}"
        return True
    
    def verify_products_sorted_by_name_descending(self):
        """Verify products are sorted Z to A"""
        names = self.get_product_names()
        assert names == sorted(names, reverse=True), f"Products are not sorted Z to A. Got: {names}"
        return True
    
    def verify_products_sorted_by_price_ascending(self):
        """Verify products are sorted by price low to high"""
        prices = self.get_product_prices()
        assert prices == sorted(prices), f"Products are not sorted by price low to high. Got: {prices}"
        return True
    
    def verify_products_sorted_by_price_descending(self):
        """Verify products are sorted by price high to low"""
        prices = self.get_product_prices()
        assert prices == sorted(prices, reverse=True), f"Products are not sorted by price high to low. Got: {prices}"
        return True
        
    