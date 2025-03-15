#Example 1:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///C:/Users/dell/Desktop/HTML_TAG_Locator.html")
driver.maximize_window()
#driver.find_element(By.TAG_NAME,"Attribute Value")
assert driver.find_element(By.TAG_NAME,"h1").text =="Welcome"
time.sleep(5)
driver.close()

#Example 2:
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
#driver.find_element(By.TAG_NAME,"Attribute Value")
print(driver.find_element(By.TAG_NAME,"a"))
time.sleep(5)
print("""First Line""")
print(driver.find_elements(By.TAG_NAME,"a"))
time.sleep(5)
print("""Second Line""")
x=driver.find_elements(By.TAG_NAME,"a")
print(len(x))
for i in x:
    print(i.text)

time.sleep(5)
print("""Third Line""")
driver.close()