#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/dell/Desktop/HTML_LINK_TEXT_Locator.html")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT"Attribute Value")
driver.find_element(By.LINK_TEXT,"Training").click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.back()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Apply for Job").click()
time.sleep(5)
driver.close()

#Example try in the following Pages :
#https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html
#https://www.selenium.dev/downloads/ ==>click on Projects