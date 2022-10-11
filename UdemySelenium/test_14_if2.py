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
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

#Sirve para validar si los botones existen o estan habilitados
button = driver.find_element_by_xpath("//button[@id='submit']")
print(button.is_enabled())

if button.is_enabled() == True:
    print("Puedes dar clic")
else:
    print("No puedes dar clic / Boton esta inhabilitado")



