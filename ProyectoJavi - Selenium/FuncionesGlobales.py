import time
from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class FuncionesGlobales():

    def __init__(self, driver):
        self.driver = driver

    def saludos(self):
        print("Bienvenido a Page Object Model")

    def tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return tiempo

    """
    def inicializarNavegador(self, url):
        self.driver = webdriver.Chrome(url)
        t = 2
    """

    def navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Pagina abierta: " + str(url))
        t = time.sleep(tiempo)
        return t






    def textBoxV1(self, xpath, texto, tiempo):
        variable = self.driver.find_element_by_xpath(xpath)
        variable.clear()
        variable.send_keys(texto)
        t = time.sleep(tiempo)
        return t

    def textBoxV2(self, xpath, texto, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(xpath)
            field.clear()
            field.send_keys(texto)
            print(f"Se ingreso tecto en el campo: {xpath} el texto: {texto}")
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + xpath)
            return t
    """
    def textId(self, id, texto, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.id, id)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(id)
            field.clear()
            field.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)
            return t
    """






    def click(self, xpath, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(xpath)
            field.click()
            print(f"Damos clic en el campo {xpath}")
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + xpath)
            return t






    #Funcion dropdown v1 por medio de XPATH
    def dropDown(self, xpath, texto, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(xpath)
            field = Select(field)
            field.select_by_visible_text(texto)

            print(f"Damos clic en el campo {xpath} con el valor {texto}")
            t = time.sleep(tiempo)


        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + xpath)
            return t

    #Funcion dropdown v1 por medio de ID
    def dropDownId(self, id, texto, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(id)
            field = Select(field)
            field.select_by_visible_text(texto)

            print(f"Damos clic en el campo {id} con el valor {texto}")
            t = time.sleep(tiempo)


        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + id)
            return t






    #Funcion dropdown v2 por medio de XPATH
    def dropDownV2(self, xpath, tipo, dato, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(xpath)
            field = Select(field)

            #Tipo puede ser "text" / "index" / "value"
            if tipo == "text":
                field.select_by_visible_text(dato)
            elif tipo == "index":
                field.select_by_index(dato)
            elif tipo == "value":
                field.select_by_value(dato)

            print(f"Damos clic en el campo {xpath}")
            t = time.sleep(tiempo)


        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + xpath)
            return t


    #Funcion dropdown v2 por medio de ID
    def dropDownV2Id(self, id, tipo, dato, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(id)
            field = Select(field)

            #Tipo puede ser "text" / "index" / "value"
            if tipo == "text":
                field.select_by_visible_text(dato)
            elif tipo == "index":
                field.select_by_index(dato)
            elif tipo == "value":
                field.select_by_value(dato)

            print(f"Damos clic en el campo {id}")
            t = time.sleep(tiempo)


        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + id)
            return t





    #upload a file
    def uploadFileXpath(self, xpath, ruta, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(xpath)
            field.send_keys(ruta)

            print(f"Se carga archivo en la ruta: {ruta}")
            t = time.sleep(tiempo)
            return t


        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + xpath)
            return t






    def radioCheck(self, xpath, tiempo):
        try:
            field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
            field = self.driver.find_element_by_xpath(xpath)
            field.click()

            print(f"Se da clic en el elemento: {xpath}")
            t = time.sleep(tiempo)
            return t


        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento: " + xpath)
            return t



    def checkBoxMultiple(self, tiempo, *args):
        try:
            for num in args:
                field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                field = self.driver.execute_script("arguments[0].scrollIntoView();", field)
                field = self.driver.find_element_by_xpath(num)
                field.click()

                print(f"Se da clic en el elemento: {num}")
                t = time.sleep(tiempo)
                return t

        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el Elemento: " + num)
            return t




