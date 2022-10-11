import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")

# se abre la pagina
driver.get("https://demoqa.com/text-box")

#Se maximiza la ventana del driver
driver.maximize_window()

#Al abir la ventana esperara 2 segundos posterior a cargar la ventana
time.sleep(3)

#Se ingresan los campos del formulario
nombre = driver.find_element_by_xpath("//input[@id='userName']")
nombre.send_keys("Rodrigo")

email = driver.find_element_by_xpath("//input[@id='userEmail']")
email.send_keys("correo@correo.com")

currentAddress = driver.find_element_by_xpath("//textarea[@id='currentAddress']")
currentAddress.send_keys("pino rudis 168, Parajes de los pinos, Ramos arizpe Coahuila Mexico")

permanentAddress = driver.find_element_by_xpath("//textarea[@id='permanentAddress']")
permanentAddress.send_keys("Altamirano 503, guayulera, Saltillo Coahuila Mexico")

#Scroll de la pagina
driver.execute_script("window.scrollTo(0,300)")

submitButton = driver.find_element_by_xpath("//button[@id='submit']")
submitButton.click()

time.sleep(3)

#se cierra el driver
driver.close()