import os
import time
# from django.test import LiveServerTestCase
from unittest import TestCase
from selenium import webdriver
# from seleniumwire import webdriver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestBase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()
    
    def login(self):
        ''' aca metemos un login pegandole al LiveServerTestCase y obtenemos un token
        y lo pasamos por headers a cada request ? como seria, o lo guardamos en cookies. nose '''
        pass

    def take_screenshot(self):
        """Take a screenshot with a defined name based on the time and the browser"""
        millis = int(round(time.time() * 1000))
        if(self.driver.name):
            driver_name = self.driver.name
        else:
            driver_name = ""
        self.driver.save_screenshot(BASE_DIR + "/../screenshots/" + driver_name + "_" + str(millis) + "_screenshots.png")

if __name__ == "__main__":
    unittest.main()
