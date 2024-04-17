from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

# this is our user information
USERNAME = 'navid'
PASSWORD = '123'

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/login/")

driver.find_element(By.ID, 'u_name').send_keys(USERNAME)
driver.find_element(By.ID, 'u_password').send_keys(PASSWORD)
driver.find_element(By.ID, 'u_password').send_keys(Keys.RETURN)

if 'Home' in driver.title:
    print('Login successful!')
else:
    print('Login failed.')
