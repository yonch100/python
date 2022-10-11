# EJERCICIO SAUCEDEMO
# POM DEL EJERCICIO TEST5_SELENIUM

class Saucedemo:
    #Captura de los xpath
    btn_login_xpath = "//input[contains(@id,'login-button')]"
    txt_user_xpath = "//input[@id='user-name']"
    txt_pss_xpath = "//input[contains(@id,'password')]"

    usrError_xpath = "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]"
    pswError_xpath = "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]"
    usrpswError_xath = "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]"

    error1 = "Epic sadface: Username is required"
    error2 = "Epic sadface: Password is required"
    error3 = "Epic sadface: Username and password do not match any user in this service"



    def __init__(self, driver):
        self.driver = driver

    def boton_login(self):
        btn_Login = self.driver.find_element_by_xpath(self.btn_login_xpath)
        btn_Login.click()

    def ingresar_usr(self, usr):
        txt_usr = self.driver.find_element_by_xpath(self.txt_user_xpath)
        txt_usr.send_keys(usr)

    def ingresar_psw(self, psw):
        txt_psw = self.driver.find_element_by_xpath(self.txt_pss_xpath)
        txt_psw.send_keys(psw)

    def limpiar_Campos(self):
        txt_usr = self.driver.find_element_by_xpath(self.txt_user_xpath)
        txt_usr.clear()
        txt_psw = self.driver.find_element_by_xpath(self.txt_pss_xpath)
        txt_psw.clear()

    #Comparacion
    def msj_usr(self):
        error1_xpath = self.driver.find_element_by_xpath(self.usrError_xpath)
        error1_msj = error1_xpath.text
        return error1_msj

    def msj_psw(self):
        error2_xpath = self.driver.find_element_by_xpath(self.pswError_xpath)
        error2_msj = error2_xpath.text
        return error2_msj

    def msj_usrpsw(self):
        error3_xpath = self.driver.find_element_by_xpath(self.usrpswError_xath)
        error3_msj = error3_xpath.text
        return error3_msj

