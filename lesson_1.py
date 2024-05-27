# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://medikom.ua/")
        driver.find_element_by_xpath("//a[@href='/doctor/']")
        driver.find_element_by_xpath("//img[@alt='logo']")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
