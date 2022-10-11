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



#Variables
t = 3


#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()



#seleccion multiple en un combobox
try:
    sistemaOperativoMultipleElement = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//select[@id='multiple-select-example1']")))
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


sistemaOperativoMultiple = Select(driver.find_element_by_xpath("//select[@id='multiple-select-example']") )
#Se seleccionan todos las opciones necesarias
sistemaOperativoMultiple.select_by_index(0)
sistemaOperativoMultiple.select_by_index(2)


time.sleep(t)
driver.close()