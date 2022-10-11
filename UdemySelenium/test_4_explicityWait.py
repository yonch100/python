import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#EXPLICITY WAIT
#Este sirve para esperar a un elemento web y hasta que aparesca interactuar con el

tiempo = 5


driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com")
driver.maximize_window()

#CODIGO EXPLICIT WAIT - importar
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='at-share-btn at-svc-facebook']")))
element.click()
#presence_of_element_located

search = driver.find_element_by_xpath("//input[@id='edit-search-block-form--2']")
search.send_keys("selenium")
time.sleep(tiempo)


#//input[@class='form-control form-text']


driver.close()

