#Example 6: Attribute
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
# time.sleep(5)
# #driver.find_element(By.CSS_SELECTOR,"Attribute Value")
# driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("Hello")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[data-test='username']").clear()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[name='user-name'][placeholder='Username']").send_keys("Hello")
# driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Tata Bye Bye")
# time.sleep(5)
# driver.close()

#Example 7: CSS Selector nth type
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("file:///C:/Users/dell/Desktop/CSS_Selector_Nth-Child.html")
# driver.maximize_window()
# time.sleep(5)
# #driver.find_element(By.CSS_SELECTOR,"Attribute Value")
# e=driver.find_element(By.CSS_SELECTOR,"ul#recordlist li:nth-of-type(2)+li")
# print(e.text)
# driver.close()

# #Example 8: CSS Selector nth type
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in/")
# driver.maximize_window()
# time.sleep(5)
# #driver.find_element(By.CSS_SELECTOR,"Attribute Value")
# #e=driver.find_element(By.CSS_SELECTOR,".mainMenu li:nth-of-type(1)+li") #to find next sibling element ==> Face element
# e=driver.find_element(By.CSS_SELECTOR,".mainMenu li:nth-child(1)") #to find child element ==Home Element
# print(e.text)
# driver.close()

#Example 9: CSS Selector first child and last child
#to find first child
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.refresh()
time.sleep(5)
driver.get("https://device.pcloudy.com/signup")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".iti__selected-flag").click()
time.sleep(5)
e=driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:first-child")
print(e.text)
e.click()
driver.close()

#Example 10: CSS Selector first child and last child
#to find last child
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://device.pcloudy.com/signup")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".iti__selected-flag").click()
time.sleep(5)
e=driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:last-child")
print(e.text)
e.click()
driver.close()