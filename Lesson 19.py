from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"

driver.get(url)

time.sleep(300)
