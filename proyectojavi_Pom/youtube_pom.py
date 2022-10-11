#Page Object Model - POM
# EJERCICIO DE ESTE POM ES EL TEST4_SELENIUM

import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Youtube:

    searchField_xpath = "//input[@id='search']"
    searchBtn_xpath = "(//yt-icon[contains(@class,'style-scope ytd-searchbox')])[2]"
    video_xpath = "//a[@id = 'video-title' and @title = 'Hayya Hayya (Better Together) | FIFA World Cup 2022™ Official Soundtrack']"

    playPauseBtn_xpath = "//button[@class = 'ytp-play-button ytp-button']"
    meGusta_xpath = "//ytd-watch-flexy[@role='main']//ytd-toggle-button-renderer[1]//a[1]//yt-formatted-string[1]"
    ordenarPor_xpath = "//div[@class='style-scope yt-dropdown-menu'][contains(.,'Ordenar por')]"
    masRecientes_xpath = "(//div[@class='item style-scope yt-dropdown-menu'][contains(.,'Más recientes primero')])[1]"

    scroll_xpath = "arguments[0].scrollIntoView();"


    def __init__(self, driver):
        self.driver = driver


    def ingresar_texto_video(self):
        textBoxVideo = self.driver.find_element_by_xpath(self.searchField_xpath)
        textBoxVideo.send_keys("Hayya Hayya")


    def boton_buscar_video(self):
        btnBuscar = self.driver.find_element_by_xpath(self.searchBtn_xpath)
        btnBuscar.click()


    def seleccionar_video(self):
        try:
            video = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.video_xpath)))
            video.click()
        except TimeoutException as ex:
            print(ex.msg)
            print("El Elemento Web No Esta Disponible:" + self.video_xpath)

    def pausar_video(self):
        try:
            playPauseBtn = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, self.playPauseBtn_xpath)))
            playPauseBtn.click()

            titulo = self.driver.title
            assert "Hayya Hayya (Better Together) | FIFA World Cup 2022™ Official Soundtrack" != titulo, "El titulo noes el validado"
            assert "watch" in self.driver.current_url, "No se encontro watch en la url de la pagina web"

        except TimeoutException as ex:
            print(ex.msg)
            print("El Elemento Web No Esta Disponible: Pausar Video: " + self.playPauseBtn_xpath)


    def clic_en_me_gusta(self):
        try:
            meGusta = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.meGusta_xpath)))
            scrollToElement = self.driver.execute_script("arguments[0].scrollIntoView();", meGusta)
            meGustaInt = int(meGusta.text.replace(",", ""))
            assert meGustaInt >= 551381, "La cantidad actual de Me gusta es menor"  # 551381

        except TimeoutException as ex:
            print(ex.msg)
            print("El Elemento Web No Esta Disponible: Me gusta: " + self.playPauseBtn_xpath)


    def ordenar_por(self):
        try:
            ordenarPor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.ordenarPor_xpath)))
            ordenarPor.click()

            try:
                masRecientes = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.masRecientes_xpath)))
                masRecientes.click()
            except TimeoutException as ex:
                print(ex.msg)
                print("El Elemento Web No Esta Disponible: Boton Mas recientes: " + self.masRecientes_xpath)

        except TimeoutException as ex:
            print(ex.msg)
            print("El Elemento Web No Esta Disponible: boton Ordenar Por: " + self.ordenarPor_xpath)

