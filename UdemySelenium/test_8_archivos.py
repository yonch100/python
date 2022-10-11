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
driver.get("http://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()


try:
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='fileinput']")))
    element = driver.find_element_by_xpath("//input[@id='fileinput']")
    #se usan las diagolanes invertidas para cargar archivos
    element.send_keys("C://Users//Yonch100//Documents//zzz_proyecto_python//imagenes//demo1.png")
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


#radio de imagen --- //input[@id='itsanimage']
radioImagen = driver.find_element_by_xpath("//input[@id='itsanimage']").click()

#radio de archivo general --- //input[@id='itsafile']
radioFile = driver.find_element_by_xpath("//input[@id='itsafile']").click()

#boton submit --- //input[@type='submit']
submitButton = driver.find_element_by_xpath("//input[@type='submit']").click()

