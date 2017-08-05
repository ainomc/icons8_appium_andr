# -*- coding: utf-8 -*
"""Module with pytest fixtures for tests"""

import os
import json
import pytest
from appium import webdriver
from logic.logic_base import LogicClick
from logic.logic_base import LogicLocate
from logic.logic_base import LogicHelper
from locators.locators_base import *


class ContextMain(object):
    """Main class with fixtures"""

    # Returns abs path relative to this file and not cwd
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p))

    my_data = json.loads(open(PATH('../param.json')).read())

    platformName = my_data['platformName']
    platformVersion = my_data['platformVersion']
    deviceName = my_data['deviceName']
    browserName = my_data['browserName']
    homepage = my_data['homepage']

    def setup_class(cls):
        """Actions before tests"""

        desired_caps = {}
        desired_caps['platformName'] = ContextMain.platformName
        desired_caps['platformVersion'] = ContextMain.platformVersion
        desired_caps['deviceName'] = ContextMain.deviceName
        desired_caps['browserName'] = ContextMain.browserName

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(4)

        cls.click = LogicClick(cls.driver)
        cls.locate = LogicLocate(cls.driver)
        cls.help = LogicHelper(cls.driver)

        cls.driver.get(ContextMain.homepage)

    def teardown_class(cls):
        """Actions after tests"""
        cls.driver.quit()


    @pytest.fixture
    def open_url(self):
        """open home page"""
        self.driver.get(ContextMain.homepage)

    @pytest.fixture
    def open_menu_toggle(self):
        """open toggle menu"""
        self.driver.get(ContextMain.homepage)
        self.click.xpath(menu_toggle)

    @pytest.fixture
    def open_icons(self):
        """OPen icons page"""
        self.driver.get(ContextMain.homepage)
        self.click.xpath(menu_toggle)
        self.click.text('Icons')

    @pytest.fixture
    def open_request(self):
        """OPen request page"""
        self.driver.get(ContextMain.homepage)
        self.click.xpath(menu_toggle)
        self.click.text('Request')

    @pytest.fixture
    def open_buy(self):
        """OPen buy page"""
        self.driver.get(ContextMain.homepage)
        self.click.xpath(menu_toggle)
        self.click.text('Buy')
