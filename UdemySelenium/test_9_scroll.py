import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#Clases importadas para el combo
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#clases de exception
from selenium.common.exceptions import TimeoutException

#implicity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("http://pixabay.com/es/")
driver.maximize_window()

# //a[@class='footButton--EuuQ7 base--1BhYu primary--1sbJ']
# //a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]
time.sleep(2)

try:
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")))
    element = driver.find_element_by_xpath("//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")
    scrollToElement = driver.execute_script("arguments[0].scrollIntoView();", element)
except TimeoutException as ex:
    print(ex.msg)
    print("Elemento Web No Esta Disponible")