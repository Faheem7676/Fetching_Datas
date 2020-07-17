from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.newsgallery.com/")

assert "NewsGallery | People's Own Media" in driver.title 

driver.find_element_by_id("guest-login-button").click()
driver.find_element_by_id("id_username").send_keys("xxxxx")
driver.find_element_by_id("id_password").send_keys("xxxxx")
driver.find_element_by_id("login_button").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='user-profile-pic']").click()
time.sleep(20)

driver.find_element(By.ID,"user-profile-pic").click()
wait=WebDriverWait(driver,10)
element=wait.until(EC.visibility_of((By.XPATH,"//*[@id='personalDetails']/div/h3/a")))

driver.find_element(By.XPATH,"//*[@id='header']/div/div/div[3]/div/div[3]/div/div/div/ul/li[2]/a").click()
#explicit_wait


