# -*- coding: utf-8 -*-
"""Logic for tests"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class LogicClick(object):
    """Click logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def xpath(self, xpath):
        """Click xpath"""
        element = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.driver.element.click()

    def text(self, link):
        """Click text"""
        element = self.driver.find_element_by_xpath('//*[text()="%s"]' % link)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[text()="%s"]' % link))).click()
        except:
            self.driver.element.click()

    def part_text(self, link):
        """Click contains text"""
        element = self.driver.find_element_by_xpath('.//*[contains(text(), "%s")]' % link)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable(
                    (By.XPATH, './/*[contains(text(), "%s")]' % link))).click()
        except:
            self.driver.element.click()


class LogicLocate(object):
    """Locate logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def xpath(self, xpath):
        """Check locate of xpath"""
        self.driver.find_element_by_xpath(xpath)

    def text(self, text):
        """Check locate of text"""
        self.driver.find_element_by_xpath('.//*[text()="%s"]' % text)

    def part_text(self, text):
        """Check locate of contains text"""
        self.driver.find_element_by_xpath('.//*[contains(text(), "%s")]' % text)


class LogicHelper(object):
    """Helper logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        """Back to the page"""
        self.driver.back()
