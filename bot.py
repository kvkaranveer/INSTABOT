from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep

class InstagramBot:
    
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.base_url="https://www.instagram.com"
    
        self.login()

    def login(self):    
        self.driver=webdriver.Chrome('C:\chromedriver\chromedriver.exe')

        self.driver.get("https://www.instagram.com")
        sleep(2)
        user_input=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        user_input.send_keys(self.username)
        
        user_password=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        user_password.send_keys(self.password)

        user_login=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
        user_login.click()
        sleep(5)
    
        turn_off=self.driver.find_element_by_class_name("yWX7d")
        turn_off.click()
        sleep(3)
  
        notification_off=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notification_off.click()
    

    def nav_user(self,user):

        self.driver.get('{}/{}'.format(self.base_url,user))
        sleep(1)
       
    def likes(self,amount):

        likes=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div")
        likes.click()
        sleep(3)
 
        
        i=1
        while i<=amount :
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
            self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            i+=1
   
    def follow(self,user):
        follow_user=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")
        follow_user.click()
   
    def message(self,user,mymessage,count):
        usermsg=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
        usermsg.click()
        sleep(2)
      
        i=1
        while i<=count:
                textarea=self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                textarea.send_keys(mymessage)
                submit=self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
                submit.click()
                # sleep(0.5)
                i+=1
    
    def comment(self,user,mycomment):
          likes=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div")
          likes.click()
          sleep(3)
          
          
          while True:
            actionChains = ActionChains(self.driver)
            actionChains.double_click(likes).perform()
        # select comment input
            self.driver.find_element_by_css_selector(".Ypffh").click()
            comment = self.driver.find_element_by_css_selector(".Ypffh")
            comment.send_keys(mycomment)
            sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()
            sleep(2)
            self.driver.find_element_by_css_selector("._65Bje").click()
            
            
 

if __name__ == "__main__":
      myusername=input("enter the username ")
      mypassword=input("enter the password ")
      user=input("enter the user which you want to follow ")
    #   mymessage=input("enter the message ")
    #   count=int(input("no of times "))
      mycomment1=input("enter the comment ")
    #   amountofcomment=int(input("no of post to comment"))
      insta_bot=InstagramBot(myusername,mypassword)       
      
      insta_bot.nav_user(user)
    #   insta_bot.likes(1)
    #   insta_bot.follow(user)
    #   insta_bot.message(user,mymessage,count)
      insta_bot.comment(user,mycomment1)