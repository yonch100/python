#EJERCICIO DEL POM NOPCOMMERCE

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#archivos importados
from proyectojavi_Pom.nopcommerce_pom import NopCommerce
from FuncionesGlobales import FuncionesGlobales

driver: WebDriver = webdriver.Chrome(r"/webdirvers/chromedriver.exe")
fg = FuncionesGlobales(driver)

def test_open_chrome():
    fg.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 3)
    driver.maximize_window()

def test_error_email():
    fg.textBoxV2("//input[contains(@id,'Email')]", "jorge@100.com", 2)
    fg.textBoxV2("//input[contains(@id,'Password')]", "jorge", 2)
    fg.click("//button[@type='submit'][contains(.,'Log in')]",2)

    error = driver.find_element_by_xpath("//li[contains(.,'No customer account found')]")
    error_txt = error.text
    assert error_txt == "No customer account found", "Mensaje de error incorrecto"

def test_no_email():
    fg.textBoxV2("//input[contains(@id,'Email')]", "", 2)
    fg.textBoxV2("//input[contains(@id,'Password')]", "", 2)
    fg.click("//button[@type='submit'][contains(.,'Log in')]",2)

    error_email = driver.find_element_by_xpath("//span[contains(@id,'Email-error')]")
    error_txt = error_email.text
    assert error_txt == "Please enter your email", "Mensaje de error incorrecto"

def test_wrong_acount():
    fg.textBoxV2("//input[contains(@id,'Email')]", "admin@yourstore.com", 2)
    fg.textBoxV2("//input[contains(@id,'Password')]", "abcde", 2)
    fg.click("//button[@type='submit'][contains(.,'Log in')]",2)

    error_noAcount = driver.find_element_by_xpath("//li[contains(.,'The credentials provided are incorrect')]")
    error_txt = error_noAcount.text
    assert error_txt == "The credentials provided are incorrect", "Mensaje de error incorrecto"

def test_login_succesfull():
    fg.textBoxV2("//input[contains(@id,'Email')]", "admin@yourstore.com", 2)
    fg.textBoxV2("//input[contains(@id,'Password')]", "admin", 2)
    fg.click("//button[@type='submit'][contains(.,'Log in')]",2)

    msj = driver.find_element_by_xpath("//h1[contains(.,'Dashboard')]")
    msj_text = msj.text
    assert msj_text == "Dashboard", "No ingresaste a la pantalla principal"

def test_driver_close():
    driver.close()

