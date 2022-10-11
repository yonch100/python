import time
import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
        driver = self.driver
        t = 2



    def test1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)

        username = driver.find_element_by_xpath("//input[contains(@id,'user-name')]").click()
        username = driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("usr100")
        time.sleep(1)

        pss = driver.find_element_by_xpath("//input[contains(@id,'password')]").click()
        pss = driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("psw100")
        time.sleep(1)

        driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
        time.sleep(3)

        errorDriver = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = errorDriver.text #Epic sadface: Username and password do not match any user in this service

        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos")
            print("Prueba 1: Ok")



    def test2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)

        #agrega un valor al campp pss
        pss = driver.find_element_by_xpath("//input[contains(@id,'password')]").click()
        pss = driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("psw100")
        time.sleep(1)

        driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
        time.sleep(3)

        #Realiza la captura del error
        errorDriver = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = errorDriver.text  # Epic sadface: Username and password do not match any user in this service

        #Realiza la validacion del error
        if error == "Epic sadface: Username is required:":
            print("Falta agregar el campo NNombre de usuario")
            print("Prueba 2: Ok")

        time.sleep(3)



    def test3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)

        # agrega un valor al campp username
        username = driver.find_element_by_xpath("//input[contains(@id,'user-name')]").click()
        username = driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("usr100")
        time.sleep(1)

        driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
        time.sleep(3)

        # Realiza la captura del error
        errorDriver = driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error = errorDriver.text  # Epic sadface: Username and password do not match any user in this service

        # Realiza la validacion del error
        if error == "Epic sadface: Password is required":
            print("Falta agregar el campo Contraseña")
            print("Prueba 3: Ok")

        time.sleep(3)



    def test5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)

        # agrega un valor al campp username
        username = driver.find_element_by_xpath("//input[contains(@id,'user-name')]").click()
        username = driver.find_element_by_xpath("//input[contains(@id,'user-name')]").send_keys("standard_user")
        time.sleep(1)

        # agrega un valor al campp pss
        pss = driver.find_element_by_xpath("//input[contains(@id,'password')]").click()
        pss = driver.find_element_by_xpath("//input[contains(@id,'password')]").send_keys("secret_sauce")
        time.sleep(1)

        driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
        time.sleep(3)

        element = driver.find_element_by_xpath("//span[@class='title'][contains(.,'Products')]")

        if element.is_displayed():
            print(f"el elemento se encuentra en pantalla: \n{element}")
        else:
            print("el elemento no se encuentra en pantalla")



    def test6(self):
        driver = self.driver
        f = Funciones


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()