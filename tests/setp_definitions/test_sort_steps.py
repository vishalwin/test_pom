from pytest_bdd import scenarios
from pytest_bdd import given, when, then  

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
def sort_name(driver):
    inventory= Inventory_Page(driver)
    inventory.select_sort_option("Name (Z to A)")
    
