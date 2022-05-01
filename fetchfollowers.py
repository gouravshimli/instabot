from logging import error
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver=webdriver.Chrome()

name=input("Enter Id")
SCROLL_PAUSE_TIME = 2
##############################################################################################################
# Function to sign in instagram account
def signIn(username,password):
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    driver.maximize_window()
    username=driver.find_element_by_name('username').send_keys(username)
    password=driver.find_element_by_name('password').send_keys(password)
    loginButon=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(6)
def startFetch(username):
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(3)
    followers=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
    time.sleep(4)
    last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)

    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height
    
    
signIn('team_military_unit','********')
startFetch(name)
