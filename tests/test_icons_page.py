# -*- coding: utf-8 -*
"""Icons page tests"""

from context.context_base import ContextMain
from locators.locators_base import *


class TestIconsPage(ContextMain):
    """Icon Page tests class"""

    def test_presents_search_field(self, open_icons):
        """Check presents of search field"""
        self.locate.xpath(icons_search_field)

    def test_presents_icons_filters(self, open_icons):
        """Check presents of icons filter"""
        self.locate.xpath(icons_filter_1)
        self.locate.xpath(icons_filter_2)
        self.locate.xpath(icons_filter_3)

    def test_presents_icon_resuilt(self, open_icons):
        """Check presents of icon on the page"""
        self.locate.xpath(icon_result)

    def test_presents_category_menu(self, open_icons):
        """Check presents of category menu"""
        self.click.xpath(category_menu)
        self.locate.text('iOS 10')
        self.locate.text('Adobe Design')