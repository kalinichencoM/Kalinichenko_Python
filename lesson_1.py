# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from selenium.webdriver.common.by import By


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    
    def test_app_dynamics_job(self):
        wd = self.wd
        self.open_home_padge(wd)
        self.find_doctor_by_name(wd, doctor_name="Адаменко")
        wd.find_element(By.XPATH, "//img[@alt='logo']").click()

    def find_doctor_by_name(self, wd, doctor_name):
        self.open_doctors_page(wd)
        wd.find_element(By.ID, "search-price").send_keys(doctor_name)

    def open_doctors_page(self, wd):
        # open doctors page
        wd.find_element(By.XPATH, "//a[@href='/doctor/']").click()

    def open_home_padge(self, wd):
        # open home page
        wd.get("https://medikom.ua/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
