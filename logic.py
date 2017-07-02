# -*- coding: utf-8 -*-
"""Logic for tests"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogicClick(object):
    """Click logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def click_xpath(self, xpath):
        """Click xpath"""
        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.driver.find_element_by_xpath(xpath).click()

    def click_text(self, link):
        """Click text"""
        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[text()="%s"]' % link))).click()
        except:
            self.driver.find_element_by_xpath('//*[text()="%s"]' % link).click()

    def click_part_text(self, link):
        """Click contains text"""
        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable(
                    (By.XPATH, './/*[contains(text(), "%s")]' % link))).click()
        except:
            self.driver.find_element_by_xpath('.//*[contains(text(), "%s")]' % link).click()


class LogicLocate(object):
    """Locate logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def locate_xpath(self, xpath):
        """Check locate of xpath"""
        self.driver.find_element_by_xpath(xpath)

    def locate_text(self, text):
        """Check locate of text"""
        self.driver.find_element_by_xpath('.//*[text()="%s"]' % text)

    def locate_part_text(self, text):
        """Check locate of contains text"""
        self.driver.find_element_by_xpath('.//*[contains(text(), "%s")]' % text)


class LogicHelper(object):
    """Helper logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        """Back to the page"""
        self.driver.back()
