from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('chromedriver')
driver.get('https://twitter.com/explore/tabs/trending')
time.sleep(2)
for i in range(3,8):
    hashtags = driver.find_element(By.XPATH,f"//div[@aria-label='Timeline: Explore']/div/div[{i}]/div/div/div/div/div[2]/span/span").text
    tweets = driver.find_element(By.XPATH,f"//div[@aria-label='Timeline: Explore']/div/div[{i}]/div/div/div/div/div[3]/span").text
    print(hashtags,' -> ',tweets)