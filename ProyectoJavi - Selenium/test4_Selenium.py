# EJERCICIO ED YOUTUBE

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from proyectojavi_Pom.youtube_pom import Youtube as Yt


#1.-Dirijirse a Youtube
driver: WebDriver = webdriver.Chrome(r"C:\Users\usuario1\Documents\pythonProject\webdirvers\chromedriver.exe")
yt = Yt(driver)

driver.get("https://youtube.com")
driver.maximize_window()

yt.ingresar_texto_video()
yt.boton_buscar_video()
yt.seleccionar_video()
yt.pausar_video()
yt.clic_en_me_gusta()
yt.ordenar_por()

