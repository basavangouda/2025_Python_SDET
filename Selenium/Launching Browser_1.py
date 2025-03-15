# Chrome Browser

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj=Service("C:/Users/dell/Downloads/Drivers/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
expected_title="Swag labs"
actual_title=driver.title
time.sleep(5)
if expected_title==actual_title:
    print("Test Pass")
else:
    print("Test Fail")
time.sleep(5)
driver.close()

# Microsoft Edge Browser
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
service_obj=Service("C:/Users/dell/Downloads/Drivers/msedgedriver.exe")
driver=webdriver.Edge(service=service_obj)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
expected_title="Swag Labs"
actual_title=driver.title
time.sleep(5)
if expected_title==actual_title:
    print("Test Pass")
else:
    print("Test Fail")
time.sleep(5)
driver.close()


# Firefox Browser
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
service_obj=Service("C:/Users/dell/Downloads/Drivers/geckodriver.exe")

options = Options()
options.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"

driver=webdriver.Firefox(service=service_obj,options=options)
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.maximize_window()
expected_title="Swag Labs"
actual_title=driver.title
time.sleep(5)
if expected_title==actual_title:
    print("Test Pass")
else:
    print("Test Fail")
time.sleep(5)
driver.close()
