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
driver.get("https://demoqa.com/")
driver.maximize_window()


titulo = driver.find_element_by_xpath("//img[@src='/images/Toolsqa.jpg']")
#print(f"¿El titulo esta desplegado?: {titulo.is_displayed()})
print(titulo.is_displayed())
print(titulo)
button = driver.find_element_by_xpath("(//div[contains(@class,'card-up')])[1]")

#para un disply activo
if titulo.is_displayed() == True:
    print("Existe la imagen")
    button.click()
    time.sleep(2)
else:
    print("El titulo no existe")

