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
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()




#SAVE CHANGES
launchModal = driver.find_element_by_xpath("(//a[@data-toggle='modal'][contains(.,'Launch modal')])[1]").click()
try:
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    element = driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[1]").click()

except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible -----------> Modal")

#CLOSE
launchModal = driver.find_element_by_xpath("(//a[@data-toggle='modal'][contains(.,'Launch modal')])[1]").click()
try:
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]")))
    element = driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Close')])[1]").click()

except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible -----------> Modal")