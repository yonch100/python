#EJERCICIO SAUCEDEMO
# EJERCICIO DEL POM SAUCEDEMO
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proyectojavi_Pom.saucedemo_pom import Saucedemo as Sd
import random
import pytest

#//input[@id='user-name']
#//input[contains(@id,'password')]
#//input[contains(@id,'login-button')]
error1 = "Epic sadface: Username is required"
error2 = "Epic sadface: Password is required"
error3 = "Epic sadface: Username and password do not match any user in this service"



#Creacion del driver - se abre la pagina
driver: WebDriver = webdriver.Chrome(r"C:\Users\usuario1\Documents\pythonProject\webdirvers\chromedriver.exe")
sd = Sd(driver)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()


"""
---------------------------------------------------------------------------------------------------------------------
TEST 1
---------------------------------------------------------------------------------------------------------------------
"""
def test_Validar_Login():
    #1.- Validacion de username
    sd.boton_login()
    assert sd.msj_usr() == "Epic sadface: Username is required", "El mensaje debe de ser: Epic sadface: Username is required"
    #screenshot = driver.save_screenshot('my_screenshot.png') ---> save a screenshot

    #2.- Valiacion de password
    sd.ingresar_usr("a")
    sd.boton_login()
    assert sd.msj_psw() == "Epic sadface: Password is required", "El mensaje debe de ser: Epic sadface: Password is required"
    sd.limpiar_Campos()

    #3.- usr y pss erroneos
    sd.ingresar_usr("a")
    sd.ingresar_psw("a")
    sd.boton_login()
    assert sd.msj_usrpsw() == "Epic sadface: Username and password do not match any user in this service", "El mensaje debe de ser: Epic sadface: Username and password do not match any user in this service"
    sd.limpiar_Campos()


"""
---------------------------------------------------------------------------------------------------------------------
TEST 2
---------------------------------------------------------------------------------------------------------------------
def test_Ingresar_Login():
txt_user = driver.find_element_by_xpath("//input[@id='user-name']")
txt_user.clear()
txt_user.send_keys("standard_user")

txt_pss = driver.find_element_by_xpath("//input[contains(@id,'password')]")
txt_pss.clear()
txt_pss.send_keys("secret_sauce")

btn_Login = driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
btn_Login.click()

element_list = []
#Dar clic aleatoriamente
try:
    driver.implicitly_wait(5)
    i = 0
    while i < 3:
        elements = driver.find_elements_by_xpath("//button[@class='btn btn_primary btn_small btn_inventory']")
        element = random.choice(elements)
        #element_list.append(element.text)
        element.click()

        #label_product = driver.find_element_by_xpath("//button[@class='btn btn_primary btn_small btn_inventory']/../../child::div/child::a/child::div[@class='inventory_item_name']")
        #print(label_product.text)
        driver.implicitly_wait(5)

        shpCar_badge = driver.find_element_by_xpath("//span[@class='shopping_cart_badge']")
        shpCar_badge_text = shpCar_badge.text
        i = int(shpCar_badge_text)

except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible")

shpCar_badge = driver.find_element_by_xpath("//a[contains(@class,'shopping_cart_link')]")
shpCar_badge.click()
"""


"""
---------------------------------------------------------------------------------------------------------------------
TEST 3
---------------------------------------------------------------------------------------------------------------------
"""

