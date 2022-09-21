from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mobile_emulation = { "deviceName": "Nexus 5" }
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome('chromedriver')

driver.get('https://www.instagram.com/')
time.sleep(2)
#driver.find_element(By.XPATH,"//*[contains(text(),'Log In')]").click()
#time.sleep(1)
driver.find_element(By.NAME,'username').send_keys('studrijit@gmail.com')
driver.find_element(By.NAME,'password').send_keys('matara1234')
time.sleep(1)
driver.find_element(By.XPATH,"//*[contains(text(),'Log In')]").click()
time.sleep(7)
driver.find_element(By.XPATH,"//*[contains(text(),'Not Now')]").click()
time.sleep(2)
#driver.find_element(By.XPATH,"//*[contains(text(),'Cancel')]").click()
#time.sleep(2)
driver.get('https://www.instagram.com/rijit99/followers/')
'''driver.find_element(By.XPATH,"//div[@class='_abp7']/div[5]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"//ul[@class=' _aa_8']/li[2]/a").click()'''

pop_up_window = WebDriverWait(
    driver, 4).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='dialog']")))
  
# Scroll till Followers list is there
while True:
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
      pop_up_window)
    time.sleep(1)
'''
time.sleep(7)
driver.find_element(By.TAG_NAME,'body').click()
time.sleep(1)
#print(driver.execute_script('return document.body.scrollHeight'))
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
while True:
    prev_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == prev_height:
        break
'''