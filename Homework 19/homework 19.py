from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://test.mensa.no/"

driver.get(url)

age1850_xpath = '//button[contains(@class,"ageselect_1850")]'
age1850_button = driver.find_element(By.XPATH, age1850_xpath)
age1850_button.click()
time.sleep(3)


time.sleep(3000)