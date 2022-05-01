import time
from selenium import webdriver
from selenium.webdriver.common.utils import find_connectable_ip
driver=webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(2)
driver.maximize_window()
username=driver.find_element_by_name('username').send_keys('faraday_jones')
password=driver.find_element_by_name('password').send_keys('**********')
loginButon=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(10)
notNow=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
time.sleep(2)
notNow2=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

# for likeing posts
# for i in range(1,5):
#     likeButton=driver.find_element_by_xpath(f'/html/body/div[1]/section/main/section/div/div[2]/div/article[{i}]/div[3]/section[1]/span[1]/button').click()
#     time.sleep(3)
#     commentArea=driver.find_element_by_xpath(f'/html/body/div[1]/section/main/section/div/div[2]/div/article[{i}]/div[3]/section[3]/div/form/textarea')
#     commentArea.click()
#     time.sleep(3)
#     commentArea=driver.find_element_by_xpath(f'/html/body/div[1]/section/main/section/div/div[2]/div/article[{i}]/div[3]/section[3]/div/form/textarea')
#     commentArea.click()
#     commentArea.send_keys('******This message is only for testing brouser automation******')
#     commentArea.submit()
#     #    
    
# comment by tag name 
tagSearch=driver.get('https://www.instagram.com/explore/tags/makeup/')
time.sleep(3)
recentPosts=driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
time.sleep(5)
for i in range(1,5):
    commentArea=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
    commentArea.click()
    commentArea=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
    time.sleep(2)
    commentArea.send_keys('Dm for shoutout @_united_beauty_')
    time.sleep(2)
    commentArea.submit()
    nextPost=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
    time.sleep(4)

# time.sleep(3)
# commentArea=driver.find_element_by_xpath(f'/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[3]/div/form/textarea')
# commentArea.click()
# time.sleep(3)
# commentArea=driver.find_element_by_xpath(f'/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[3]/div/form/textarea')
# commentArea.click()
# commentArea.send_keys('******This message is only for testing brouser automation******')
# commentArea.submit()







# likeButton=driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article[2]/div[3]/section[1]/span[1]/button').click()
# for commenting post


# /html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button
# /html/body/div[1]/section/main/section/div/div[2]/div/article[2]/div[3]/section[1]/span[1]/button
# /html/body/div[1]/section/main/section/div/div[2]/div/article[3]/div[3]/section[1]/span[1]/button
# /html/body/div[1]/section/main/section/div/div[2]/div/article[4]/div[3]/section[1]/span[1]/button

# /html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button
# /html/body/div[1]/section/main/section/div/div[2]/div/article[2]/div[3]/section[1]/span[1]/button
# /html/body/div[1]/section/main/section/div/div[2]/div/article[3]/div[3]/section[1]/span[1]/button
# /html/body/div[1]/section/main/section/div/div[2]/div/article[4]/div[3]/section[1]/span[1]/button

# # paths of comment section
# /html/body/div[1]/section/main/section/div/div[2]/div/article[2]/div[3]/section[3]/div/form/textarea
# /html/body/div[1]/section/main/section/div/div[2]/div/article[3]/div[3]/section[3]/div/form/textarea

# path of the full post 
# /html/body/div[1]/section/main/section/div/div[2]/div/article[3]
# /html/body/div[1]/section/main/section/div/div[2]/div/article[4]
# /html/body/div[1]/section/main/section/div/div[2]/div/article[4]
# /html/body/div[1]/section/main/section/div/div[2]/div/article[4]
# /html/body/div[1]/section/main/section/div/div[2]/div/article[5]
# /html/body/div[1]/section/main/section/div/div[2]/div/article[5]

# i=0
# while(i<5):
#     time.sleep(5)
#     likeButton=driver.find_elements_by_class_name('fr66n')
#     for items in likeButton:
#         like=likeButton[items].text
#         like.click()
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     i=i+1
# print(len(likeButton))
# print(type(likeButton))
# for i in range(len(likeButton)):
#     print(likeButton[i])

# textArea.send_keys("******Don't worry this message is for testing automation******")
# time.sleep(3)
# textArea.submit()
