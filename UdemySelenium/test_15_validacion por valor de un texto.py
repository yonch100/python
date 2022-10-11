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
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

btnSend = driver.find_element_by_xpath("//button[@class='btn btn-default']") #//button[@type='submit'][contains(.,'Send')]
btnSend.click()

'''
Validacion de los textos de las variables
'''
firstNameMsj = driver.find_element_by_xpath("//small[@class='help-block'][contains(.,'Please supply your first name')]")
textFirstNameMsj = firstNameMsj.text
#print(f"El valor de el error es: {textFirstNameMsj}")

ApellidoPaternoMsj = driver.find_element_by_xpath("//small[@class='help-block'][contains(.,'Please supply your last name')]")
textApellidoPaterno = ApellidoPaternoMsj.text

"""
VALIDACION DE CAMPOS
"""
#Nombre
if textFirstNameMsj == "Please supply your first name":
    #print("Falta ingresar el campo First Name")
    firstName = driver.find_element_by_xpath("//input[@name='first_name']").click()
    firstName = driver.find_element_by_xpath("//input[@name='first_name']").send_keys("Jorge Omar")
    time.sleep(3)
    print("Nombre correcto")
else:
    print("Falta el nombre")

#Apellido paterno
if textApellidoPaterno == "Please supply your last name":
    #print("Falta ingresar el campo last Name")
    lastName = driver.find_element_by_xpath("//input[@name='last_name']").click()
    lastName = driver.find_element_by_xpath("//input[@name='last_name']").send_keys("Hernandez Flores")
    time.sleep(3)
    print("Apellido correcto")
else:
    print("Falta el apellido")

 