############ регистрация аккаунта

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

email_address = driver.find_element_by_id("reg_email")
email_address.send_keys("yyy@mail.ru")
password = driver.find_element_by_id("reg_password")
time.sleep(3)
password.send_keys("2parol1#2P555")
time.sleep(5)
register = driver.find_element_by_name("register")
register.click()
driver.quit()

############  логин в систему

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

login = driver.find_element_by_id("username")
login.send_keys("yyy@mail.ru")
password =driver.find_element_by_id("password")
password.send_keys("2parol1#2P555")
login_btn = driver.find_element_by_name("login")
login_btn.click()
logout = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout>a")) )
driver.quit()

