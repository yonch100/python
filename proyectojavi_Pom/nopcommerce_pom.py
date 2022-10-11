#POM DEL EJERCICIO LOGIN

base_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"

class NopCommerce:
    #Xpaths
    email_xpath = "//input[contains(@id,'Email')]"
    password_xpath = "//input[contains(@id,'Password')]"
    boton_xpath = "//button[@type='submit'][contains(.,'Log in')]"

    error1_xpath = "//li[contains(.,'No customer account found')]"
    error2_xpath = "//span[contains(@id,'Email-error')]"
    error3_xpath = "//li[contains(.,'The credentials provided are incorrect')]"
    dashboard_label_xpath = "//h1[contains(.,'Dashboard')]"


    def __init__(self, driver):
        self.driver = driver

    def ingreasr_usr(self, email):
        txt_email = self.driver.find_element_by_xpath(self.email_xpath)
        txt_email.send_keys(email)

    def ingresar_psw(self, psw):
        txt_psw = self.driver.find_element_by_xpath(self.password_xpath)
        txt_psw.send_keys(psw)

    def clic_login(self):
        boton_login = self.driver.find_element_by_xpath(self.boton_xpath)
        boton_login.click()