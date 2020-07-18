from selenium import webdriver
driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")

driver.get("https://facebook.com/")

html=driver.page_source

print(html)