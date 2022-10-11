import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(3)

#elements by
#Se ingresan los campos del formulario
nombre = driver.find_element(By.ID,"userName")
nombre.send_keys("Rodrigo")

email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
email.send_keys("correo@correo.com")


driver.close()