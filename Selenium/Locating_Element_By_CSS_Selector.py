#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)
#driver.find_element(By.CSS_SELECTOR,"Attribute Value")
driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("Hello")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Tata Bye Bye")
time.sleep(5)
driver.close()

#Example 2:
#parent tag> child tag
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"div>input#username").send_keys("Hello")
time.sleep(5)
driver.close()

#Example 3:
# parent tag child tag
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
driver.maximize_window()
time.sleep(5)
e=driver.find_element(By.CSS_SELECTOR,"div a")
print(e.text)
time.sleep(5)
driver.close()

#Example 4: CSS selector class
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("Hello")
time.sleep(5)
driver.close()

#Example 5 : We can combine class and ID to find the unique element
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://app.hubspot.com/login/legacy")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input#password.form-control.private-form__control").send_keys("Hello")
time.sleep(5)
driver.close()