from selenium import webdriver
from PIL import Image

driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")

url="https://stage.newsgallery.com/"

driver.get(url)

driver.save_screenshot("image.png")
image=Image.open("image.png")

image.show()