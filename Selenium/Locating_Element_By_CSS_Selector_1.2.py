#Example 11: CSS Selector Matching a Prefix (Starts with) ====> ^
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://device.pcloudy.com/signup")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[id^='fna']").send_keys("QACircle Software Training Academy")
time.sleep(5)
driver.close()

#Example 12: CSS Selector Matching a Prefix (Starts with) ====> ^
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[class^='submit']").click()
time.sleep(5)
assert driver.find_element(By.CSS_SELECTOR,"h3[data-test^='error']").text=="Epic sadface: Username is required"
driver.close()

#Example 13: CSS Selector Matching a Prefix (Starts with) ====> ^
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"div[class^='name-la']").text)
time.sleep(5)
driver.close()