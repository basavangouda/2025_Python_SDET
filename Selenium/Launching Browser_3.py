# Install Webdriver-Manager

# Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.qacircle.com/")
driver.maximize_window()
expected_title="QACircle Software Training Academy"
actual_title=driver.title

if expected_title==actual_title:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()

# Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.qacircle.com/")
driver.maximize_window()
expected_title="QACircle Software Training Academy"
actual_title=driver.title

if expected_title==actual_title:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()

# Edge
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.qacircle.com/")
driver.maximize_window()
expected_title="QACircle Software Training Academy"
actual_title=driver.title

if expected_title==actual_title:
    print("Test Pass")
else:
    print("Test Fail")
driver.close()