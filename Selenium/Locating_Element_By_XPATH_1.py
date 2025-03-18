import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Example 1: Absolute Xpath
# driver=webdriver.Chrome()
# driver.get("file:///C:/Users/dell/Desktop/Absolute_XPath.html")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH,"html/body/form/input[3]").clear()
# time.sleep(5)
# driver.find_element(By.XPATH,"html/body/form/input[3]").send_keys("example@gmail.com")
# time.sleep(5)
# driver.close()

#Example 2 :https://www.saucedemo.com/

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("example@gmail.com")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("Hello")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='login-button']").click()
time.sleep(5)

e=driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
print(e.text)

assert e.text=="Epic sadface: Username and password do not match any user in this service"

driver.close()