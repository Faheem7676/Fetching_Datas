from selenium import webdriver
import time

driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")

website_url="https://www.newsgallery.com/"
driver.get(website_url)

refreshrate=int(15)
#this would keep running untill you stop the compiler
while True:
    time.sleep(refreshrate)
    driver.refresh()