import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#Clases importadas para el combo
from selenium import webdriver
from selenium.webdriver.support.ui import Select


#Variables
t = 1

#se abre el explorador
driver: WebDriver = webdriver.Chrome(r"C:\Users\Yonch100\Documents\zzz_proyecto_python\Chromedriver\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/reservation.php")
driver.maximize_window()

#Seleccionar todos los combos
#Primero se realiza un clic sobre el combo y luego se selecciona la opcion deseada



#Passengers
passengers = driver.find_element_by_xpath("//select[@name='passCount']").click()
time.sleep(t)
passengers = Select(driver.find_element_by_xpath("//select[@name='passCount']") )
#passengers.select_by_value("2")
passengers.select_by_index(3)



#Departing From
departingFrom = driver.find_element_by_xpath("//select[@name='fromPort']").click()
time.sleep(t)
departingFrom = Select(driver.find_element_by_xpath("//select[@name='fromPort']") )
#passengers.select_by_value("2")
departingFrom.select_by_index(5)



#on
on = driver.find_element_by_xpath("//select[@name='fromMonth']").click()
time.sleep(t)
on = Select(driver.find_element_by_xpath("//select[@name='fromMonth']") )
#passengers.select_by_value("2")
on.select_by_index(11)

#onDate
onDay = driver.find_element_by_xpath("//select[@name='fromDay']").click()
time.sleep(t)
onDay = Select(driver.find_element_by_xpath("//select[@name='fromDay']") )
#passengers.select_by_value("2")
onDay.select_by_index(30)



#arrivingIn
arrivingIn = driver.find_element_by_xpath("//select[@name='toPort']").click()
time.sleep(t)
arrivingIn = Select(driver.find_element_by_xpath("//select[@name='toPort']") )
#passengers.select_by_value("2")
arrivingIn.select_by_index(9)



#Returning
returning = driver.find_element_by_xpath("//select[@name='fromMonth']").click()
time.sleep(t)
returning = Select(driver.find_element_by_xpath("//select[@name='fromMonth']") )
#passengers.select_by_value("2")
returning.select_by_index(1)

#Returningdate
returningday = driver.find_element_by_xpath("//select[@name='toDay']").click()
time.sleep(t)
returningday = Select(driver.find_element_by_xpath("//select[@name='toDay']") )
#passengers.select_by_value("2")
returningday.select_by_index(4)



#airlane
airlane = driver.find_element_by_xpath("//select[@name='airline']").click()
time.sleep(t)
airlane = Select(driver.find_element_by_xpath("//select[@name='airline']") )
#passengers.select_by_value("2")
airlane.select_by_index(3)



continueButton = driver.find_element_by_xpath("//input[@name='findFlights']")
continueButton.click()
