# -*- coding: utf-8 -*
"""Buy page tests"""

from context.context_base import ContextMain
from locators.locators_base import *


class TestBuyPage(ContextMain):
    """Buy Page tests class"""


    def test_presents_unlimited_plan(self, open_buy):
        """Check presents of Unlimited Plan"""
        self.locate.part_text('Unlimited Plan')
        self.locate.part_text('Buy for $19.90/month')

    def test_presents_free_plan(self, open_buy):
        """Check presents of Free plan"""
        self.locate.part_text('Free')
        self.locate.part_text('Try for Free')

    def test_presents_service_integration_plan(self, open_buy):
        """Check presents of Service Integration plan"""
        self.locate.part_text('Service Integration')
        self.locate.part_text('Starting from $100/month')

    def test_presents_video_in_buy_page(self, open_buy):
        """Check presents of video on buy page"""
        self.locate.xpath(video_in_buy_page)

    def test_presents_info_text_in_buy_page(self, open_buy):
        """Check presents of info text in buy page"""
        self.locate.part_text('Paid License Summary')
        self.locate.part_text('Standard License Agreement')
        self.locate.part_text('Permitted Uses')
        self.locate.part_text('Prohibited Uses for all Licenses')
        self.locate.part_text("What's Included")
        self.locate.part_text('All Plans Except PNG Cobra')
        self.locate.part_text('New Icons and Support')
        self.locate.part_text('Built-in Editing Tools')
        self.locate.part_text('Web App')
        self.locate.part_text('Icons8 App for Mac and Windows')
        self.locate.part_text('FAQ on Icons8 App')