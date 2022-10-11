import time
from selenium.webdriver.chrome.webdriver import WebDriver
#Clases importadas para el combo
from selenium import webdriver
#implicity
from selenium.webdriver.common.by import By



#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

#obtension de toso los lins de la pagina actual
#todos los liks cuenta con la variable a en el xpath
numeroDeLinks = driver.find_elements(By.TAG_NAME, "a")
print("El numero de links que se encuentran en la pagina es: ", len(numeroDeLinks) )

for num in numeroDeLinks: print(num.text)

time.sleep(3)
driver.find_element_by_link_text("Date pickers").click()
time.sleep(1)
driver.find_element_by_link_text("JQuery Date Picker").click()
