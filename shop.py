############# отображение страницы товара

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

login = driver.find_element_by_id("username")
login.send_keys("yyy@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("2parol1#2P555")
login_btn = driver.find_element_by_name("login")
login_btn.click()

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()
HTML5_book = driver.find_element_by_css_selector(".post-181 .attachment-shop_catalog")
HTML5_book.click()
name = driver.find_element_by_css_selector(".product_title.entry-title")
element_get_text = name.text
assert element_get_text == "HTML5 Forms"
driver.quit()

############# количество товаров в категории

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

login = driver.find_element_by_id("username")
login.send_keys("yyy@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("2parol1#2P555")
login_btn = driver.find_element_by_name("login")
login_btn.click()

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()

html_cat = driver.find_element_by_css_selector(".cat-item-19>a")
html_cat.click()
time.sleep(3)

items_count = driver.find_elements_by_css_selector("a>h3")
if len(items_count) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))

driver.quit()

################# сортировка товаров

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

login = driver.find_element_by_id("username")
login.send_keys("yyy@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("2parol1#2P555")
login_btn = driver.find_element_by_name("login")
login_btn.click()

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()

status_selector = driver.find_element_by_name("orderby")
status_selector_sort = status_selector.get_attribute("value")
if status_selector_sort == "menu_order":
    print("Выбран вариант сортировки по умолчанию")
else:
    print("Другой вариант сортировки")

select = Select(status_selector)
select.select_by_value("price-desc")

status_selector = driver.find_element_by_name("orderby")
status_selector_sort = status_selector.get_attribute("value")
if status_selector_sort == "price-desc":
    print("Выбран вариант сортировки от большего к меньшему")
else:
    print("Другой вариант сортировки")

driver.quit()

################# отображение, скидка товара

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
password = driver.find_element_by_id("password")
password.send_keys("2parol1#2P555")
login_btn = driver.find_element_by_name("login")
login_btn.click()

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()

android_quick = driver.find_element_by_css_selector("img[title = 'Android Quick Start Guide']")
android_quick.click()

old_price = driver.find_element_by_css_selector(".price del>span")
old_price_text = old_price.text
new_price = driver.find_element_by_css_selector(".price ins>span")
new_price_text = new_price.text

assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"

book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")) )
book_cover.click()

book_cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
book_cover_close.click()

driver.quit()

################# проверка цены в корзине

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()

#добавить в корзину можно только книгу Mastering JavaScript
add_to_basket = driver.find_element_by_css_selector(".post-165 .button")
add_to_basket.click()

items_basket = driver.find_elements_by_css_selector(".cartcontents")
assert len(items_basket) == 1
time.sleep(3)

price = driver.find_element_by_css_selector(".wpmenucart-contents>.amount ")
price_text = price.text
assert price_text == "₹350.00"

basket = driver.find_element_by_css_selector("[title='View your shopping cart']")
basket.click()

subtotal_price = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .amount")) )

total_price = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".order-total .amount")) )

driver.quit()

################### работа в корзине

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()

driver.execute_script("window.scrollBy(0, 300);")
#добавить в корзину можно только книгу Mastering JavaScript
add_to_basket = driver.find_element_by_css_selector(".post-165 .button")
add_to_basket.click()
time.sleep(3)

basket = driver.find_element_by_css_selector("[title='View your shopping cart']")
basket.click()
time.sleep(3)

book_remove = driver.find_element_by_css_selector("[title='Remove this item']")
book_remove.click()
time.sleep(3)
undo = driver.find_element_by_link_text("Undo?")
undo.click()

loc_quantity = driver.find_element_by_css_selector("[title='Qty']")
loc_quantity.clear()
time.sleep(3)
loc_quantity.send_keys("3")

update_basket_btn = driver.find_element_by_name("update_cart")
update_basket_btn.click()

loc_quantity_num = loc_quantity.get_attribute("value")
assert loc_quantity_num == "3"
time.sleep(3)

apply_coupon_btn = driver.find_element_by_name("apply_coupon")
apply_coupon_btn.click()

coupon_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code.") )

driver.quit()

##################### покупка товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

shop_btn = driver.find_element_by_css_selector(".main-nav>li:nth-child(1)>a")
shop_btn.click()

driver.execute_script("window.scrollBy(0, 300);")
#добавить в корзину можно только книгу Mastering JavaScript
add_to_basket = driver.find_element_by_css_selector(".post-165 .button")
add_to_basket.click()
time.sleep(3)

basket = driver.find_element_by_css_selector("[title='View your shopping cart']")
basket.click()

proceed_to_checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")) )
proceed_to_checkout.click()

first_name_basket = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")) )
first_name_basket.send_keys("Curochka")
last_name_basket = driver.find_element_by_id("billing_last_name")
last_name_basket.send_keys("Ryaba")
email_address = driver.find_element_by_id("billing_email")
email_address.send_keys("yyy@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("000000000")
selector_country = driver.find_element_by_id("s2id_billing_country")
selector_country.click()
country_field = driver.find_element_by_id("s2id_autogen1_search")
country_field.send_keys("Isle of Man")
country_variant = driver.find_element_by_id("select2-result-label-467")
country_variant.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Main street")
city = driver.find_element_by_id("billing_city")
city.send_keys("Main city")
state_county = driver.find_element_by_id("billing_state")
state_county.send_keys("Isle of Man")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("111111")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
option = driver.find_element_by_css_selector("[value='cheque']")
option.click()

place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()

thank_you_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received.") )

check_payments_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments") )

driver.quit()




































































