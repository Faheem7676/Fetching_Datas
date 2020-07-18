from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from time import sleep


class NewsGallery:

    def __init__(self,username,password):
        #these lines will help if someone faces issues like 
        # chrome closes after execution 
        self.opts=webdriver.ChromeOptions("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")
        self.opts.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=self.opts)
        self.driver.maximize_window()

        #username passwrod
        self.username=username
        self.password=password

        #open Newsgallery login page
        self.driver.get("https://www.newsgallery.com/")
        sleep(2)

        #automatically enter username and password
        self.driver.find_element(By.ID,"guest-login-button").click()
        self.driver.find_element(By.ID,"id_username").send_keys(self.username)
        self.driver.find_element(By.ID,"id_password").send_keys(self.password)
        #click on login button
        self.driver.find_element(By.ID,"login_button").click()

obj1=NewsGallery("faheem","faheem")
