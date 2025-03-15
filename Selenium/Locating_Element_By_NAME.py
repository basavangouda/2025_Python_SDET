#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#driver.find_element(By.NAME,"Attribute Value")
time.sleep(5)
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.NAME,"login-button").click()
time.sleep(5)
driver.close()