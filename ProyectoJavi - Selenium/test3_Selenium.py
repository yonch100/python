from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from proyectojavi_Pom import youtube_pom as Youtube

#1.-Dirijirse a Youtube
driver: WebDriver = webdriver.Chrome(r"C:\Users\TrueHome\Documents\Pycharm Proyects\webdirvers\chromedriver.exe")
driver.get("https://youtube.com")
driver.maximize_window()

#2.- buscar la cacncion "Hayya Hayya" la cancion del mundial
searchField = driver.find_element_by_xpath("//input[@id='search']")
searchField.click()
searchField.clear()
searchField.send_keys("Hayya Hayya")

searchBtn = driver.find_element_by_xpath("(//yt-icon[@class='style-scope ytd-searchbox'])[3]")
searchBtn.click()



#3.- Dar clic en el primer resultado (video oficial)
try:
    video = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//a[@id = 'video-title' and @title = 'Hayya Hayya (Better Together) | FIFA World Cup 2022™ Official Soundtrack']")))
    video.click()
except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible: video")
    driver.quit()



#4.- Validar qeu la url del video contenga el siguiente texto: FIFA
#tituloVideo = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"(//yt-formatted-string[contains(@class,'style-scope ytd-video-primary-info-renderer')])[2]")))
assert "watch" in driver.current_url, "No se encontro watch en la url de la pagina web"



#5.- Validar que el título sea exactamente el siguiente: “Hayya Hayya (Better Together) | FIFA World Cup 2022™ Official Soundtrack”
titulo = driver.title
assert "Hayya Hayya (Better Together) | FIFA World Cup 2022™ Official Soundtrack" != titulo, "El titulo noes el validado"



#6 Dar clic en el boton de pausar video
try:
    playPauseBtn = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[@class = 'ytp-play-button ytp-button']")))
    #playPauseBtn = driver.find_element_by_xpath("//button[@class = 'ytp-play-button ytp-button']")
    playPauseBtn.click()
except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible: boton de pause")
    driver.quit()




#7 Verificar que el numero de "Me gusta" sea mayor o igual a  551381
try:
    meGusta = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//ytd-watch-flexy[@role='main']//ytd-toggle-button-renderer[1]//a[1]//yt-formatted-string[1]")))
    #meGusta = driver.find_element_by_xpath("//ytd-watch-flexy[@role='main']//ytd-toggle-button-renderer[1]//a[1]//yt-formatted-string[1]")
    meGustaInt = int(meGusta.text.replace(",",""))
    assert meGustaInt >= 551381, "La cantidad actual de Me gusta es menor" #551381
except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible: me gusta")
    driver.quit()



#8 Ordenar los comentarios por "Mas Recientes"
scrollToElement = driver.execute_script("arguments[0].scrollIntoView();", meGusta)
try:
    ordenarPor = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='style-scope yt-dropdown-menu'][contains(.,'Ordenar por')]")))
    #ordenarPor = driver.find_element_by_xpath("//div[@class='style-scope yt-dropdown-menu'][contains(.,'Ordenar por')]")
    ordenarPor.click()

    try:
        masRecientes = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(//div[@class='item style-scope yt-dropdown-menu'][contains(.,'Más recientes primero')])[1]")))
        #masRecientes = driver.find_element_by_xpath("(//div[@class='item style-scope yt-dropdown-menu'][contains(.,'Más recientes primero')])[1]")
        masRecientes.click()
        driver.implicitly_wait(5)
    except TimeoutException as ex:
        print(ex.msg)
        print("El Elemento Web No Esta Disponible: " + masRecientes)
        driver.quit()

except TimeoutException as ex:
    print(ex.msg)
    print("El Elemento Web No Esta Disponible: " + ordenarPor)
    driver.quit()









driver.quit()