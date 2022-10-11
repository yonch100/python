import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

from UdemyUnitTest.FuncionesGlobales import FuncionesGlobales
from UdemyUnitTest.FuncionesLogin import FuncionesLogin

class EjecucionFunciones(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\TrueHome\Documents\Pycharm Proyects\webdirvers\chromedriver.exe")
        t = 2



    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.navegar("https://www.saucedemo.com/", 3)
        f.textBoxV1("//input[@id='user-name']", "Omar", 3)



    def test2(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.navegar("https://www.saucedemo.com/", 3)

        f.textBoxV2("//input[@id='user-name']", "Omar", 3)
        f.textBoxV2("//input[@id='password']", "Omar", 3)
        f.click("//input[@id='login-button']", 3)



    def test3(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        login1 = FuncionesLogin(driver)
        login1.Login("https://www.saucedemo.com/", "omar", "pssOmar", 3)



    def test4(self):
        driver = self.driver

        funcionGlobal = FuncionesGlobales(driver)
        funcionGlobal.navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", 3)

        #funcionGlobal.dropDown("//select[contains(@id,'select-demo')]", "Sunday", 3) #dropdown V1

        funcionGlobal.dropDownV2("//select[contains(@id,'select-demo')]", "text", "Sunday", 3) #dropDown V2 - text
        funcionGlobal.dropDownV2("//select[contains(@id,'select-demo')]", "index", 5, 3)  # dropDown V2 - index
        funcionGlobal.dropDownV2("//select[contains(@id,'select-demo')]", "value", "Tuesday", 3)  # dropDown V2 - value


    def test5(self):
        driver = self.driver
        funcionglobal1 = FuncionesGlobales(driver)
        funcionglobal1.navegar("http://testpages.herokuapp.com/styled/file-upload-test.html", 3)

        # funcionglobal1.click("//input[contains(@id,'fileinput')]", 3)
        funcionglobal1.uploadFileXpath("//input[contains(@id,'fileinput')]", "C://Users//Yonch100//Documents//zzz_proyecto_python//imagenes//demo1.png", 3)


        funcionglobal1.click("//input[contains(@id,'itsanimage')]", 3)
        #image --- //input[contains(@id,'itsanimage')]

        #funcionglobal1.click("//input[contains(@id,'itsafile')]", 3)
        #A general file - //input[contains(@id,'itsafile')]

        funcionglobal1.click("//input[contains(@type,'submit')]", 3)
        #upload --- //input[contains(@type,'submit')]



    def test6(self):
        driver = self.driver
        funcionglobal1 = FuncionesGlobales(driver)
        funcionglobal1.navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", 3)

        funcionglobal1.radioCheck("//input[contains(@id,'isAgeSelected')]", 3)



    def test7(self):
        driver = self.driver
        funcionglobal1 = FuncionesGlobales(driver)
        funcionglobal1.navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html", 3)
        for n in range(2,5):
            funcionglobal1.checkBoxMultiple(1, "(//input[contains(@type,'checkbox')])[" + str(n) +"]")



    def test8(self):
        driver = self.driver
        funcionglobal1 = FuncionesGlobales(driver)
        funcionglobal1.navegar("https://opensource-demo.orangehrmlive.com/", 3)

        funcionglobal1.textBoxV2("//input[contains(@id,'txtUsername')]", "Admin", 2)
        funcionglobal1.textBoxV2("//input[contains(@id,'txtPassword')]", "admin123", 2)
        funcionglobal1.click("//input[contains(@id,'btnLogin')]",2)

        #xpath de primer menu
        adminMenu = driver.find_element_by_xpath("//b[contains(.,'Admin')]")
        usrManagementSubMenu = driver.find_element_by_xpath("//b[contains(.,'Admin')]")
        usrsSubMenu = driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")

        #"//a[@id='menu_admin_viewSystemUsers']"
        #"//a[@href='/index.php/admin/viewSystemUsers']"

        action1 = ActionChains(driver)
        action1.move_to_element(adminMenu).click().perform()
        #action1.move_to_element(usrManagementSubMenu).click().perform()
        #action1.move_to_element(usrsSubMenu).perform()


