
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('chromedriver')

driver.get('https://www.instagram.com/')
time.sleep(2)
driver.find_element(By.NAME,'username').send_keys('studrijit@gmail.com')
driver.find_element(By.NAME,'password').send_keys('matara1234')
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
time.sleep(7)
driver.get('https://www.instagram.com/vickykaushal09/')
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='_ac7v _aang']/div[1]/a").click()
time.sleep(2)
try:
    driver.find_element(By.XPATH,"//span[@class='_aamw']/button/div[2]/span/*[name()='svg']").click()
except:
    print('no new post')
    driver.quit()
    
    
