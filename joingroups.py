import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver=webdriver.Chrome()
for i in range(20070,21000):
    try:
        search=driver.get(f"https://realgrouplinks.com/group.php?id={i}")
        print(i)
        time.sleep(4)
        joinchat=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/a").click()
        time.sleep(3)
    except:
        continue