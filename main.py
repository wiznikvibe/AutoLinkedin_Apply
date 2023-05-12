from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

class EasyApply:

    def __init__(self,data):
        """
        Parameters Initialised here
        """
        self.email = data['email']
        self.password = data['password']
        self.keyword = data['keyword']
        self.location = data['location']

        self.driver = wb.Chrome(service=Service(data['driver_path']),chrome_options=wb.ChromeOptions().add_experimental_option("detach", True)) # wb.Chrome(data['driver_path'])
        
    def login_linked(self):
        """
        This function logs into linkedin using our email and password
        """
        # Get to Linkedin Login Page
        self.driver.get("http://www.linkedin.com\login")

        # Here we find elements by their name     
        login_email = self.driver.find_element("name","session_key")
        login_email.clear() # We clear the field to introduce new text
        # sends in the email value
        login_email.send_keys(self.email)
        
        login_passsword = self.driver.find_element("name","session_password")
        login_passsword.clear()
        login_passsword.send_keys(self.password)
        login_passsword.send_keys(Keys.RETURN)

    def job_search(self):
        """
        This function goes into
        """
        jobs_link = self.driver.get("https://www.linkedin.com/jobs/")
        

        search_box = self.driver.find_element(By.XPATH,'//input[@aria-label="Search by title, skill, or company"]') 
        search_box.clear()
        search_box.send_keys(self.keyword)

        location_box = self.driver.find_element(By.XPATH,'//input[@aria-label="City, state, or zip code"]') 
        location_box.clear()
        location_box.send_keys(self.location)

        search_button = self.driver.find_element(By.XPATH, '//button[@aria-label="Search"]')
        search_button.click()












if __name__ == '__main__':
    with open('config.json') as config:
        data = json.load(config)
    
    bot = EasyApply(data)
    bot.login_linked()
    bot.job_search()