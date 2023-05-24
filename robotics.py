from time import sleep
from RPA.Browser.Selenium import Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re


br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)
    
    def search_scientist_by_name(self, scientistName):
        self.open_webpage("https://www.wikipedia.org")
        search_input = br.driver.find_element(By.NAME,"search")
        search_input.clear()
        search_input.send_keys(scientistName)
        search_input.send_keys(Keys.RETURN)
    
    def get_birth_date(self):
        dates = br.driver.find_element(By.CLASS_NAME,'infobox').find_elements(By.CLASS_NAME,'infobox-data')  
        birthdate_text = dates[0].text
        birthdate_text=birthdate_text.replace('\n',' ')
        for i in birthdate_text.split(" "):
            if(len(i)==4 and re.match("\d{4}",i)):
                return int(i)
    
    def get_death_date(self):
        deathdate_text = br.driver.find_element(By.CLASS_NAME,'infobox').find_elements(By.CLASS_NAME,'infobox-data')[1].text
        deathdate_text=deathdate_text.replace('\n',' ')
        for i in deathdate_text.split(" "):
            if(len(i)==4 and re.match("\d{4}",i)):
                return int(i)
    
    def get_summary(self):
        i=2
        while(i<20):
            s="//p["+str(i)+"]"
            summary = br.driver.find_element(By.XPATH,s).text
            if(len(summary.strip())<20):
                i=i+1
                continue
            return summary