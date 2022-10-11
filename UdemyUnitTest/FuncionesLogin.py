import unittest
import time
from telnetlib import EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from UdemyUnitTest.FuncionesGlobales import FuncionesGlobales

class FuncionesLogin():

    def __init__(self, driver):
        self.driver = driver

    def Login(self, url, name, pss, time):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.navegar(url, time)

        f.textBoxV2("//input[@id='user-name']", name, time)
        f.textBoxV2("//input[@id='password']", pss, time)
        f.click("//input[@id='login-button']", time)


