# Chrome Browser
import time
from selenium import webdriver
driver=webdriver.Chrome()
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
driver=webdriver.Edge()
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
driver=webdriver.Firefox()
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
