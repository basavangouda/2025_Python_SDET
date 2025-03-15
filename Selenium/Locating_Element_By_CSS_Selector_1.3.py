#Example 14: CSS Selector Match a suffix(Ends with) ====> $
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://device.pcloudy.com/signup")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[name$='name']").send_keys("QACircle Software Training Academy")
time.sleep(5)
driver.close()

#Example 15:  CSS Selector Match a suffix(Ends with) ====> $
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder$='name']").send_keys("Hello")
time.sleep(5)
driver.close()

#Example 16:  CSS Selector Match a suffix(Ends with) ====> $
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"button[class$='ch-button']").text)
time.sleep(5)
driver.close()