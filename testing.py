from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# yahoo
elem = driver.find_element(By.XPATH,'//*[@id="searchbox_input"]')
time.sleep(3)
elem.send_keys('flipkart')
elem.send_keys(Keys.ENTER)
time.sleep(4)
elem = driver.find_element(By.XPATH, '//*[@id="r1-0"]/div[2]/div/div/a/div/p/span').click()
time.sleep(2)
elem = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
elem.send_keys('mobails')
elem.send_keys(Keys.ENTER)
time.sleep(2)
driver.execute_script("window.scrollTo(0,1200)")
time.sleep(2)
clickable_elements = driver.find_elements(By.XPATH, '//a | //button')
if clickable_elements:
    random_element = random.choice(clickable_elements)
    random_element.click()
    time.sleep(5)
else:
    print("No clickable elements found")
elem = driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[3]/form/button')
time.sleep(2)
driver.close()