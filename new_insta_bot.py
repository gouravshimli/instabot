
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
notWorkingId=['united_beauty_team1','team_military_unit',]
userNames=["thisbossmom","janiejmoss","silvia_m_gallegos_","jacki.watson.96","mscolada23","thalia_1_9_9_0","predsprncss","katherine_wilson344","italbratt","theamaria_75","harlandmica","jazzie1_","lyleloveyazzie","ozchick2020","dee.mahon.98","amy_franklin_524","isaiahbella1112","aprilhurt0503","teresa.marie81","djp1ayer","kirstylee.91","adiktive_datghettolv","tutta_tei_hey","shellshockcbd","lauren.nicole26__"]
username2=["team_military_soldiers2",'faraday_jones3','team_military_office','team_military1',"team_military2",'united_beauty_py','team_military_ocean',]
password2="*******"
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


def commentStart(username):
    driver.get(f"https://www.instagram.com/{username}")
    time.sleep(3)
    try:
        divs=driver.find_elements_by_class_name("_9AhH0")
        for div in divs:
            div.click()             
            time.sleep(5)          
            commentArea=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            commentArea.click()                
            commentArea=driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
            commentArea.send_keys('Dm for shoutout @_military_soldiers')
            time.sleep(2)
            commentArea.submit()
            time.sleep(4)
            return 1
    except NoSuchElementException:
        return 0
        
driver=webdriver.Chrome()
i=0
signIn(username2[i],password2)
count=0
for item in userNames:
    if count>=10:
        i=i+1
        driver.quit()
        driver=webdriver.Chrome()
        signIn(username2[i],password2)
        print(username2[i])
        count=0
    
    result=commentStart(item)
    if result:
        count=count+1
        with open("successComment.txt","a") as f:
            f.write(item + "\n")
        print(count)
        continue
    else:
        print(item)
        