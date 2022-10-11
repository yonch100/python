import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r"C:\Users\TrueHome\Documents\Pycharm Proyects\webdirvers\chromedriver.exe")

try:
    driver.get("https://www.truehome.com.mx/valua-tu-casa-con-truehome")
    driver.maximize_window()

    firstName = driver.find_element_by_xpath("//input[@name='first_name']")
    firstName.click()
    firstName.clear()
    firstName.send_Keys("Jorge Omar")

    lastName = driver.find_element_by_xpath("//input[@name='last_name']")
    lastName.click()
    lastName.clear()
    lastName.send_Keys("Herandez")

    secondLastName = driver.find_element_by_xpath("//input[@name='second_last_name']")
    secondLastName.click()
    secondLastName.clear()
    secondLastName.send_Keys("Flores")

    celular = driver.find_element_by_xpath("//input[@name='mobile_number']")
    celular.click()
    celular.clear()
    celular.send_keys("8442394257")

    correoElectronico = driver.find_element_by_xpath("//input[@name='email']")
    correoElectronico.click()
    correoElectronico.clear()
    correoElectronico.send_keys("correo@correo.com")

except:
    driver.quit()
finally:
    driver.quit()

