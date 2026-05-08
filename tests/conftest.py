import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

def pytest_addoption(parser):
   parser.addoption(
      "--browser",
      action="store",
      default ="chrome"
   )
@pytest.fixture(scope="function")
def driver(request):
   browser = request.config.getoption("--browser", default="chrome").lower()
   if browser == "chrome":
      driver = webdriver.Chrome()
   elif browser == "edge":
      driver = webdriver.Edge()
   elif browser == "firefox":
      driver = webdriver.Firefox()
   else:
      raise ValueError("Unsupported browser {browser}")
   
   driver.maximize_window()
   
   driver.implicitly_wait(5)
   
   yield driver
   
   driver.quit()