from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
'''Uncomment the below line when running in linux'''
from pyvirtualdisplay import Display
import time, os
from random import choice
global tweet
global base

i5='rze00389@eoopy.com'


id_m = i5
no_of_tweets=200

id1=id_m
id2=str('41354141')
base=651
new_base=1

tw1=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials1.txt')
tweet1=''
for n in tw1:
    tweet1=tweet1+n
tw2=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials2.txt')
tweet2=''
for n in tw2:
    tweet2=tweet2+n
tw3=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials3.txt')
tweet3=''
for n in tw3:
    tweet3=tweet3+n
tw4=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials4.txt')
tweet4=''
for n in tw4:
    tweet4=tweet4+n
tw5=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials5.txt')
tweet5=''
for n in tw5:
    tweet5=tweet5+n
tw6=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials6.txt')
tweet6=''
for n in tw6:
    tweet6=tweet6+n
tw7=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials7.txt')
tweet7=''
for n in tw7:
    tweet7=tweet7+n
tw8=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials8.txt')
tweet8=''
for n in tw8:
    tweet8=tweet8+n
tw9=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials9.txt')
tweet9=''
for n in tw9:
    tweet9=tweet9+n
tw10=open(r'C:\Users\damod\Desktop\EASY TWEET\11\credentials10.txt')
tweet10=''
for n in tw10:
    tweet10=tweet10+n

tweet=[tweet1,tweet2,tweet3,tweet4,tweet5,tweet6,tweet7,tweet8,tweet9,tweet10]

def base2(new_base):
    return new_base*100
        

class Twitterbot:  
    def __init__(self, email, password):
        self.email = email
        self.password = password
        # initializing chrome options
        chrome_options = Options()
        # adding the path to the chrome driver and 
        # integrating chrome_options with the bot
        self.bot = webdriver.Chrome(
            executable_path = os.path.join(os.getcwd(),'chromedriver.exe'),
            options = chrome_options
                                    )
    def login(self):
        """
            Method for signing in the user 
            with the provided email and password.
        """
  
        bot = self.bot
        # fetches the login page
        bot.get('https://twitter.com/login')
        # adjust the sleep time according to your internet speed
        time.sleep(1)
  
        email = bot.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = bot.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        )
  
        # sends the email to the email input
        email.send_keys(self.email)
        # sends the password to the password input
        password.send_keys(self.password)
        time.sleep(2)
        # executes RETURN key action
        password.send_keys(Keys.RETURN)
  
    def draft(self,tweet,base,no_of_tweets,new_base):  
        bot = self.bot
        time.sleep(2)
        # fetches the latest tweets with the provided hashtag
        bot.get('https://twitter.com/home')
        time.sleep(3)
        for n in range(no_of_tweets):
            tweet1=tweet
            tweet=str(choice(tweet))
            tweet=tweet+' '+str(base)
            draft=str(tweet)
            time.sleep(1.5)
            time.sleep(1.5)
            try:
                write=bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
            except:
                print('MISTAKE 2'*10)
            time.sleep(0.8)
            try:
                write=bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys(draft)
            except:
                print('MISTAKE 2'*10)
            time.sleep(1.5)
            try:
                cross=bot.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
            except:
                print('MISTAKE 3'*10)
            time.sleep(2)
            print('NO = ',base)
            tweet=tweet1
            base=base+1
        file_of_base=open('base.txt','w')
        file_of_base.write(str(base))
        file_of_base.close()
        exit()

            
bot = Twitterbot(id1,id2)
# loging in
bot.login()
# calling like_retweet function
bot.draft(tweet,base,no_of_tweets,new_base)
