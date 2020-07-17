from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")

driver.get("https://www.newsgallery.com/")

driver.maximize_window()

wait=WebDriverWait(driver,10)
element=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='subdivision-cards']/article[1]/div/div/div/div[1]/header/h3/a")))
print(element.is_displayed())