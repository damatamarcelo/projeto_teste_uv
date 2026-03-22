from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sethings import url, user, password
from time import sleep


# Configurações do Selenium
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
sleep(3)

# Tela de login
user_input = driver.find_element(By.ID, ":r2:")
user_input.send_keys(user)
sleep(1)
password_input = driver.find_element(By.ID, ":r3:")
password_input.send_keys(password)
sleep(1)
password_input.send_keys(Keys.ENTER)
sleep(10)
