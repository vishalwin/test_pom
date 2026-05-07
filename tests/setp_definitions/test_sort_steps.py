from pytest_bdd import scenarios
from pytest_bdd import given, when, then  
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import Inventory_Page

scenarios("../features/sort.feature")

@given("user open login page")
def open_login(driver):
    # create LoginPage object
    login = LoginPage(driver)
    login.open_url()
    
@when("user enters valid credetials")
def valid_login(driver):
    login = LoginPage(driver)
    login.login_site("standard_user","secret_sauce")
    
@when("user selects \"Name (A to Z)\" from dropdown")
def sort_name_a_to_z(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Name (A to Z)")

@when("user selects \"Name (Z to A)\" from dropdown")
def sort_name_z_to_a(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Name (Z to A)")

@when("user selects \"Price (low to high)\" from dropdown")
def sort_price_low_to_high(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Price (low to high)")

@when("user selects \"Price (high to low)\" from dropdown")
def sort_price_high_to_low(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Price (high to low)")

@then("products should sort successfully by name in ascending order")
def verify_name_ascending(driver):
    product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [item.text for item in product_names]
    assert names == sorted(names), f"Products are not sorted A to Z. Got: {names}"

@then("products should sort successfully by name in descending order")
def verify_name_descending(driver):
    product_names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [item.text for item in product_names]
    assert names == sorted(names, reverse=True), f"Products are not sorted Z to A. Got: {names}"

@then("products should sort successfully by price in ascending order")
def verify_price_ascending(driver):
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(item.text.replace("$", "")) for item in price_elements]
    assert prices == sorted(prices), f"Products are not sorted by price low to high. Got: {prices}"

@then("products should sort successfully by price in descending order")
def verify_price_descending(driver):
    price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(item.text.replace("$", "")) for item in price_elements]
    assert prices == sorted(prices, reverse=True), f"Products are not sorted by price high to low. Got: {prices}"
    
