import time
from selenium import webdriver
# path="C:\\Users\\goura\\OneDrive\\Documents\\crome"
driver=webdriver.Chrome()
# driver.get('https://www.instagram.com/')
driver.get('https://www.instagram.com/accounts/login/')
username=driver.find_element_by_name('username')
password=driver.find_element_by_name('password')
username.send_keys('gourav_shimli')
password.send_keys('jcnruad@2432')
loginButton=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
loginButton.click()
time.sleep(20)
driver.set_window_position(0,0)
driver.set_window_size(1350,745)
driver.get('https://www.instagram.com/explore/tags/gymlife/')
post=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
post.click()
# commentIcon=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button/div/svg')
# commentIcon.click()
textArea=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
textArea.send_keys('Dm for shotout @_united_beauty_')
time.sleep(1)
postComment=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')
postComment.click()
driver.get_window_position()
# /html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea
# /html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea