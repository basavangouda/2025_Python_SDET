#Example 17: CSS Selector Substring(Contains)  ====> *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://device.pcloudy.com/signup")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder*='ness Em']").send_keys("QACircle Software Training Academy")
time.sleep(5)
driver.close()

#Example 18: CSS Selector Substring(Contains)  ====> *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder*='assw']").send_keys("Hello")
time.sleep(5)
driver.close()

#Example 19:  CSS Selector match word(Contains)  ====> ~
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mamaearth.in/")
driver.maximize_window()
time.sleep(5)
list=driver.find_elements(By.CSS_SELECTOR,"li[class~='category']")
print(list)
print(len(list))
for i in list:
    print(i.text)
time.sleep(5)
driver.close()