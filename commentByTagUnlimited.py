import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
username=['united_beauty_py','faraday_jones','united_beauty_team1','faraday_jones2','makeup_beauty_py','faraday_jones3',]
password=['********','********','********','********','********','********']
tags=["Instagram","Tags","Here"]
# tags=['bisexual','transgirl','transgender','lashes','makeup','lgbt','gay','lesbian']
li=["You are more fun than anyone or anything I know, including bubble wrap","You are the most perfect you there is","You are enough","You are one of the strongest people I know","You look great today","You have the best smile","Your outlook on life is amazing","You just light up the room","You make a bigger impact than you realize","You are always so helpful","You have the best laugh","You are always so helpful","You have the best laugh","I appreciate our friendship","Your inside is even more beautiful than your outside","You just glow","I love the way you bring out the best in people","Our family/school/community/church is better because you are part of it","You bring out the best in the rest of us","You inspire me","Nothing can stop you","You just made my day","You make me float up like I’m on millions of bubbles (We got this one from one of our kids after he got a new coat"]
# driver=webdriver.Chrome()
##############################################################################################################
# Function to sign in instagram account
def signIn(username,password):
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    driver.maximize_window()
    username=driver.find_element_by_name('username').send_keys(username)
    password=driver.find_element_by_name('password').send_keys(password)
    loginButon=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(5)
##############################################################################################################
#Comment on posts of given tags
def commentByTagName(tag):
    # randomTag=random.choice(tags)
    tagSearch=driver.get(f'https://www.instagram.com/explore/tags/{tag}/')
    time.sleep(2)
    divs=driver.find_elements_by_class_name("_9AhH0")
    i=0
    for div in divs:
        if i<=10:
            i=i+1
            continue
        else:
            div.click() 
            time.sleep(5)                             
            for i in range(0,3):
                try:
                    commentArea=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                    commentArea.click()                    
                    commentArea=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                    commentArea.send_keys('Dm for shoutout @_united_beauty_')
                    time.sleep(1.5)
                    commentArea.submit()
                    time.sleep(4)
                    nextPost=driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a').click()
                    time.sleep(3)
                except NoSuchElementException:
                    time.sleep(3)
                    nextPost=driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a').click()
                    time.sleep(5)
                except:
                    commentByTagName(tag)
##############################################################################################################
#Function for like all the post of a specific persion            
def likeAllPosts(username):
    driver.get(f'https://www.instagram.com/{username}/')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div/div[2]').click()
    time.sleep(4)              
    for i in range(1,275):
        time.sleep(4)
        try:
            likeButton=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(1)
            nextButton=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
        except NoSuchElementException:
            nextButton=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
            time.sleep(1)
        except:
            print("Other mistake in program")
#########################################################################################################
# Function for commment on all the posts of a spicific persion 
def commentOnAllPosts(username):
    # li=[]
    # with open("comments.txt","r") as f:
    #     str=f.read()
    #     li.append(str.split("."))
    driver.get(f'https://www.instagram.com/{username}/')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div/div[2]').click()
    time.sleep(4)   
    # commentArea=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')    
    for i in range(20):
        try:
            randomComment=random.choice(li)
            commentArea=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            commentArea.click()
            commentArea=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            commentArea.send_keys(f'{randomComment}')
            time.sleep(4)
            commentArea.submit()
            time.sleep(3)
            nextPost=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
            time.sleep(3)
        except NoSuchElementException:
            time.sleep(3)
            nextPost=driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
            time.sleep(5)
        except:
            return 
            # driver.get('https://www.instagram.com/')
for i in range(3):
    for i in range(0,5):
        driver=webdriver.Chrome()
        signIn(username[i],password[i])
        for items in tags:
            commentByTagName(items)
            
        # commentOnAllPosts("virgin_jordi")    
        # likeAllPosts('virgin_jordi')
        driver.close()
        time.sleep(2)
        print(i)
    print('Sleeping...........for 15-20 Minutes!!!')
    time.sleep(1000)
     
# query='mango'
# res = requests.get('https://www.google.com?q=' + query)
# print(res.text)
    