import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#Variables
t = 5

#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()


expandTreeButton = driver.find_element_by_xpath("//button[@class='rct-option rct-option-expand-all']")
expandTreeButton.click()



time.sleep(t)
driver.close()