from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# Driver for chrome at https://sites.google.com/chromium.org/driver/
# Driver for firefox at https://github.com/mozilla/geckodriver/releases
service = Service(executable_path="./resources/geckodriver.exe")
driver = webdriver.Firefox(service=service)


driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie_id = "bigCookie"
cookies_id = "cookies"
cookies_count = 0
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 500).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.ID, cookie_id)))
WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.ID, cookie_id)))
cookie = driver.find_element(By.ID, cookie_id)


while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)
    for i in range(4):
        product_price = driver.find_element(
            By.ID, product_price_prefix + str(i)
        ).text.replace(",", "")
        if not product_price.isdigit():
            continue

        product_price = int(product_price)
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
