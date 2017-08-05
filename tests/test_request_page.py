# -*- coding: utf-8 -*
"""Request page tests"""

from context.context_base import ContextMain
from locators.locators_base import *


class TestRequestPage(ContextMain):
    """Request Page tests class"""


    def test_presents_fast_for_50(self, open_request):
        """Check "Fast for $50/icon" """
        self.click.text('Fast for $50/icon')
        self.locate.text('How Fast Is It?')
        self.locate.text('How Much Is It?')
        self.locate.text('Where Do I Start?')

    def test_presents_hot_ideas(self, open_request):
        """Check Hot Ideas list"""
        self.locate.text('Hot Ideas')
        self.locate.xpath(idea)

    def test_presents_latest_ideas(self, open_request):
        """Check Hot Ideas list"""
        self.click.part_text('Latest Ideas')
        self.locate.xpath(idea)

    def test_presents_popular_ideas(self, open_request):
        """Check Popular Ideas list"""
        self.click.part_text('Popular Ideas')
        self.locate.xpath(idea)