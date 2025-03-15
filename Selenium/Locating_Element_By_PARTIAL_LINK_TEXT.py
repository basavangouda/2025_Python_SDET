#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/downloads/")
driver.maximize_window()
time.sleep(5)
#driver.find_element(By.PARTIAL_LINK_TEXT,"Attribute Value")
driver.find_element(By.PARTIAL_LINK_TEXT,"Proj").click()
time.sleep(5)
driver.close()