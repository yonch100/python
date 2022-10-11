from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver: WebDriver = webdriver.Chrome(r"C:\Users\TrueHome\Documents\Pycharm Proyects\webdirvers\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Users\TrueHome\Documents\Pycharm Proyects\webdirvers\chromedriver.exe")

try:
    driver.get("https://www.google.com")
    driver.maximize_window()

    #elementos
    textBoxBusqueda = driver.find_element_by_xpath("//input[@title='Buscar']")
    buscarConGoogle = driver.find_element_by_xpath("//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")

    textBoxBusqueda.click()
    textBoxBusqueda.clear()
    textBoxBusqueda.send_keys("hola")
    textBoxBusqueda.send_keys(Keys.ENTER)
    #buscarConGoogle.click()
    input()

except:
    #Cerrar el navegador, la ventana enfocada
    #driver.close()
    #cierra todas las instancias de chrome
    driver.quit()
finally:
    driver.quit()
