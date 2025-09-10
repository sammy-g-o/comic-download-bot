from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

name = input()
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


browser = driver.get("https://getcomics.org/")

WebDriverWait(driver,5).until(
    expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Search'))
)
search = driver.find_element(By.PARTIAL_LINK_TEXT, 'Search')
search.click()


WebDriverWait(driver,5).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, 'query'))
)


search_bar = driver.find_element(By.CLASS_NAME, 'query')
search_bar.send_keys(f"{name}" + Keys.ENTER)



time.sleep(10.0)
driver.quit()
