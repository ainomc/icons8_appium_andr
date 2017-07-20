# -*- coding: utf-8 -*
"""Module with pytest fixtures for tests"""

import pytest
from appium import webdriver
from logic import LogicClick
from logic import LogicLocate
from logic import LogicHelper
from locators import *


class ContextMain(object):
    """Main class with fixtures"""


    def setup_class(cls):
        """Actions before tests"""
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'deviceName': 'Android Emulator',
            'browserName': 'Chrome'
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(4)

        cls.click = LogicClick(cls.driver)
        cls.locate = LogicLocate(cls.driver)
        cls.help = LogicHelper(cls.driver)

        cls.driver.get('https://demo.icons8.com/')

    def teardown_class(cls):
        """Actions after tests"""
        cls.driver.quit()


    @pytest.fixture
    def open_url(self):
        """Actions before each test"""
        self.driver.get('https://demo.icons8.com/')

    @pytest.fixture
    def open_menu_toggle(self):
        self.driver.get('https://demo.icons8.com/')
        self.click.click_xpath(menu_toggle)

    @pytest.fixture
    def open_icons(self):
        self.driver.get('https://demo.icons8.com/')
        self.click.click_xpath(menu_toggle)
        self.click.click_text('Icons')

    @pytest.fixture
    def open_request(self):
        self.driver.get('https://demo.icons8.com/')
        self.click.click_xpath(menu_toggle)
        self.click.click_text('Request')

    @pytest.fixture
    def open_buy(self):
        self.driver.get('https://demo.icons8.com/')
        self.click.click_xpath(menu_toggle)
        self.click.click_text('Buy')
