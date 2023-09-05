from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("debuggerAddress","localhost:9222")
service = ChromeService(executable_path='/home/yasashibp/Documents/ngoding/project/forexPph/env/chromedriver-linux64/chromedriver') 


driver = webdriver.Chrome(service=service,options=options)


element = driver.find_element(By.CSS_SELECTOR,'div.lastContainer-JWoJqCpY > span.last-JWoJqCpY.js-symbol-last') #hari

print(element.text)
