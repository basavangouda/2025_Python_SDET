#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#driver.find_element(By.ID,"Attribute Value")
driver.find_element(By.ID,"user-name").send_keys("qacircle")
time.sleep(5)
driver.close()

##Example 2:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
#driver.find_element(By.ID,"Attribute Value")
print(driver.find_element(By.ID,"category").text)
time.sleep(5)
driver.find_element(By.ID,"category").click()
time.sleep(5)
driver.close()
