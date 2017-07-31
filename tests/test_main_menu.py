# -*- coding: utf-8 -*
"""Main menu tests"""

from context.context_base import ContextMain
from locators.locators_base import *


class TestMainMenu(ContextMain):
    """Main menu tests class"""

    def test_open_Icons_from_menu(self, open_menu_toggle):
        """Open Icons from left side menu"""
        self.click.text('Icons')
        self.locate.text("New Icons")

    def test_open_Request_from_menu(self, open_menu_toggle):
        """Open Request from left side menu"""
        self.click.text('Request')
        self.locate.text("Request Icons")

    def test_open_Buy_from_menu(self, open_menu_toggle):
        """Open Buy from left side menu"""
        self.click.text('Buy')
        self.locate.text("Paid or Free, You Are Our Hero!")

    def test_presents_imassage_stickers_in_menu(self, open_menu_toggle):
        """Open Search from left side menu"""
        self.locate.text('iMessage Stickers')

    def test_open_Icon_Search_AI_from_menu(self, open_menu_toggle):
        """Open Search from left side menu"""
        self.click.text('Icon Search AI')
        self.locate.text("Draw an icon (Rough is OK):")

    def test_open_Blog_from_menu(self, open_menu_toggle):
        """Open Blog from left side menu"""
        self.click.text('Blog')
        self.locate.xpath(blog_list_news)

    def test_open_Register_from_menu(self, open_menu_toggle):
        """Open Register from left side menu"""
        self.click.part_text('Register')
        self.locate.part_text('Register at Icons8')

    def test_open_Login_from_menu(self, open_menu_toggle):
        """Open Login from left side menu"""
        self.click.part_text('Login')
        self.locate.text('Login to Icons8')

    def test_open_lang_menu_from_menu(self, open_menu_toggle):
        """Open Language menu from left side menu"""
        self.click.xpath(lang_menu)
        self.locate.part_text('Chinese')
        self.locate.part_text('Spanish')
        self.locate.part_text('Russian')
        self.locate.part_text('German')