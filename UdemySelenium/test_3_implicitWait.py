import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#IMPLICIT WAIT
#El el tiempo que nos da o permite la pagina para identificar los elemtos de una pagina web.
#Hasta que encuentre un elemento que este cargando en la pagina lo va a disparar si no dejara el tiempo implicito
#si el objeto lo encuentra rapidamente la ejecucion del codigo contiua, si no lo encuentra se tomara el tiempo en ()


driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)

t = 1
time.sleep(t)

#Se ingresan los campos del formulario
nombre = driver.find_element_by_xpath("//input[@id='userName']")
nombre.send_keys("Omar")
time.sleep(t)

email = driver.find_element_by_xpath("//input[@id='userEmail']")
email.send_keys("correo@correo.com")
time.sleep(t)

currentAddress = driver.find_element_by_xpath("//textarea[@id='currentAddress']")
currentAddress.send_keys("pino rudis 168, Parajes de los pinos, Ramos arizpe Coahuila Mexico")
time.sleep(t)

permanentAddress = driver.find_element_by_xpath("//textarea[@id='permanentAddress']")
permanentAddress.send_keys("Altamirano 503, guayulera, Saltillo Coahuila Mexico")
time.sleep(t)

driver.close()