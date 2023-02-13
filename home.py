import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby = driver.find_element_by_css_selector(".post-160 .button")
selenium_ruby.click()
rewiews = driver.find_element_by_css_selector(".reviews_tab>a")
rewiews.click()
stars = driver.find_element_by_css_selector(".stars .star-5")
stars.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Marina")
email = driver.find_element_by_id("email")
email.send_keys("ooo@gmail.com")
driver.find_element_by_name("submit").click()
driver.quit()
