#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#driver.find_element(By.CLASS_NAME,"Attribute Value")
driver.find_element(By.CLASS_NAME,"form_input").send_keys("Hello")
time.sleep(5)
driver.close()

#Example 2:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php")
driver.maximize_window()
#driver.find_element(By.CLASS_NAME,"Attribute Value")
assert driver.find_element(By.CLASS_NAME,"_6j.mvm._6wk._6wl._58mi._3ma._6o._6v").text =="Sign Up"
print("Matching")
time.sleep(5)
driver.find_element(By.CLASS_NAME,"_6j.mvm._6wk._6wl._58mi._3ma._6o._6v").click()
time.sleep(5)
driver.close()

#Example 3:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://hubspot.com/")
driver.maximize_window()
#driver.find_element(By.CLASS_NAME,"Attribute Value")
time.sleep(5)
driver.find_element(By.CLASS_NAME,"banner-close-btn").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"global-nav-logo.-static").click()
time.sleep(10)
driver.close()

#Example 4:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/dell/Desktop/HTML_Class_Locator.html")
driver.maximize_window()
#driver.find_element(By.CLASS_NAME,"Attribute Value")
time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"content").text)
driver.close()

