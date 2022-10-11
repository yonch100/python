from selenium.webdriver.chrome.webdriver import WebDriver

#Clases importadas para el combo
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#clases de exception
from selenium.common.exceptions import TimeoutException

#implicity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()


#VALIDAMOS QUE EL BOTON SEND EXISTA Y LE DAMOS CLIC PARA VER LOS CAMPOS OBLIGATORIOS
try:
    firstNamefield = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,"//input[@name='first_name']")))
    firstNamefield = driver.find_element_by_xpath("//input[@name='first_name']")
    print("El Elemento Web Existe")
    scrollToElement = driver.execute_script("arguments[0].scrollIntoView();", firstNamefield)
    # time.sleep(3)
    # scrollToElement= driver.execute_script("scroll(0, 0);")
except TimeoutException as ex:
    print(ex.msg)
    print("El Wlemento Web No Esta Disponible")

#Se ingresan los campos del formulario
firstName = driver.find_element_by_xpath("//input[@name='first_name']").click()
firstName = driver.find_element_by_xpath("//input[@name='first_name']").send_keys("Jorge Omar")

lastName = driver.find_element_by_xpath("//input[@name='last_name']").click()
lastName = driver.find_element_by_xpath("//input[@name='last_name']").send_keys("Hernandez Flores")

email = driver.find_element_by_xpath("//input[@name='email']").click()
email = driver.find_element_by_xpath("//input[@name='email']").send_keys("correo@correo.com")

phoneNumber = driver.find_element_by_xpath("//input[@name='phone']").click()
phoneNumber = driver.find_element_by_xpath("//input[@name='phone']").send_keys("8441989878")

adress = driver.find_element_by_xpath("//input[@name='address']").click()
adress = driver.find_element_by_xpath("//input[@name='address']").send_keys("pino silvestre 100")

city = driver.find_element_by_xpath("//input[@name='city']").click()
city = driver.find_element_by_xpath("//input[@name='city']").send_keys("Saltillo")

passengers = Select(driver.find_element_by_xpath("//select[@name='state']") )
passengers.select_by_index(22)

zipCode = driver.find_element_by_xpath("//input[@name='zip']").click()
zipCode = driver.find_element_by_xpath("//input[@name='zip']").send_keys("25000")

webSite = driver.find_element_by_xpath("//input[@name='website']").click()
webSite = driver.find_element_by_xpath("//input[@name='website']").send_keys("www.facebook.com/yonch100")


yesRadio = driver.find_element_by_xpath("//input[@value='yes']").click()
noRadio = driver.find_element_by_xpath("//input[@value='no']").click()


coments = driver.find_element_by_xpath("//textarea[@name='comment']").click()
coments = driver.find_element_by_xpath("//textarea[@name='comment']").send_keys("No comments -------------------------------------------------------------------")


submitButton = driver.find_element_by_xpath("//button[@class='btn btn-default']").click()





