# -*- coding: utf-8 -*
"""Main tests module"""

import time
from context import ContextMain
from locators import *

# python3 -m pytest -v tests.py -s


class TestHomePage(ContextMain):
    """Main tests class"""

    def test_homepage_ui_items_1(self, open_url):
        """Check home page ui presents"""
        self.locate.xpath(menu_toggle)
        self.locate.part_text('Free Flat Icons')
        self.locate.xpath(search_field)
        self.locate.part_text('Most Popular')
        self.locate.part_text('View all...')
        self.locate.xpath(first_category_icon)
        self.locate.xpath(first_landing_colors)
        self.locate.part_text('For iOS, Windows, and Android')
        self.locate.xpath(first_search_type)

    def test_homepage_ui_items_2(self, open_url):
        """Check home page ui presents"""
        self.locate.part_text('Features for UI Designers and Developers')
        self.locate.part_text('Single Style')
        self.locate.part_text('Editable Vectors')
        self.locate.part_text('Fonts Generator')
        self.locate.part_text('Icon Recoloring')
        self.locate.part_text('Mac&Win Apps')
        self.locate.part_text('HTML Embedding')
        self.locate.xpath(icon9_video)
        self.locate.part_text('Daily Updates Guided by Your Ideas')

    def test_homepage_ui_items_3(self, open_url):
        """Check home page ui presents"""
        self.locate.part_text('Free Apps for the Web, Mac, and Windows')
        self.click.text('Mac')
        self.locate.xpath(free_app_mac_bar)
        self.click.text('Windows')
        self.locate.xpath(free_app_win_bar)
        self.locate.text('Download')
        self.locate.xpath(free_app_win_bar)
        self.locate.xpath(first_company_in_bar)
        self.locate.part_text('The Community Loves Icons8')
        self.locate.part_text('Pinterest')
        self.locate.part_text('Icons by Category')
        self.locate.part_text('Social Media Icons')

    def test_footer_about(self, open_url):
        """Check About module in home page footer"""
        self.locate.text('About')
        self.locate.text('Business Model')
        self.locate.text('Team')
        self.locate.text('Our Open Source Projects')

    def test_footer_Ideas_for_Icons_popular(self, open_url):
        """Check Popular button in home page footer"""
        self.locate.text('Ideas for Icons')
        self.click.text('Popular')
        self.locate.text('Request Icons')

    def test_footer_Ideas_for_Icons_new(self, open_url):
        """Check New button in home page footer"""
        self.click.text('New')
        self.locate.text('Request Icons')

    def test_footer_Ideas_for_Icons_submit(self, open_url):
        """Check Submit button in home page footer"""
        self.click.text('Submit')
        self.locate.text('Request Icons')

    def test_footer_support_faq(self, open_url):
        """Check FAQ button in home page footer"""
        self.locate.text('Support')
        self.click.text('FAQ')
        self.locate.text('Advice and answers from the Icons8 Team')

    def test_footer_support_contact_us(self, open_url):
        """Check Contact us button in home page footer"""
        self.click.text('Contact us')
        self.locate.text('Contact Icons8')

    def test_footer_news_and_social_medium(self, open_url):
        """Check Medium button in home page footer"""
        self.locate.text('News and Social')
        self.locate.text('Blog')
        self.click.part_text('Medium')
        self.locate.text('ICONOGRAPHY')

    def test_footer_licenses_free_license(self, open_url):
        """"Check Free Licenses button in home page footer"""
        self.locate.text('Licenses')
        self.click.text('Free License')
        self.locate.part_text('Use Icons for Free')
        self.locate.part_text('Why to Link?')
        self.locate.part_text('Where to Put the Link?')
        self.locate.part_text('Websites')
        self.locate.part_text('Desktop Apps')
        self.locate.part_text('Mobile Apps')
        self.locate.part_text('Open Source')

    def test_footer_licenses_buy_full_license(self, open_url):
        """Check Full License button in home page footer"""
        self.click.text('Buy Full License')
        self.locate.part_text('Paid or Free, You Are Our Hero!')
        self.locate.part_text('Unlimited Plan')
        self.locate.part_text('Free')
        self.locate.part_text('Service Integration')
        self.locate.part_text('Paid License Summary')
        self.locate.part_text('Permitted Uses')
        self.locate.part_text('Prohibited Uses for all Licenses')
        self.locate.part_text("What's Included")
        self.locate.part_text("Built-in Editing Tools")

    def test_footer_developers_github(self, open_url):
        """Check GitHub button in home page footer"""
        self.locate.text('Developers')
        self.locate.part_text('Free Icons for Open Source')
        self.click.text('GitHub')
        self.locate.part_text('Repositories')

    def test_footer_developers_api(self, open_url):
        """Check API button in home page footer"""
        self.click.text('API')
        self.locate.part_text('Icons8 API allows us to search and obtain')

    def test_footer_privacy_policy(self, open_url):
        """Check Privacy Policy button in home page footer"""
        self.click.text('Privacy Policy')
        self.locate.part_text('Our Privacy Policy was last updated')
        self.locate.text('Your Privacy')
        self.locate.text('Definitions')
        self.locate.text('Information We Collect')
        self.locate.text('Computer Information Collected')
        self.locate.text('How We Use Your Information')
        self.locate.text('Opt-Out')
        self.locate.text('Links to Other Websites')
        self.locate.text('Security')
        self.locate.text('Privacy Policy Updates')
        self.locate.part_text('Questions About Our Privacy Practices')

    def test_footer_terms_and_conditions(self, open_url):
        """Check Terms and Conditions button in home page footer"""
        self.click.text('Terms and Conditions')
        self.locate.part_text('This web page represents a legal document')
        self.locate.text('Definitions')
        self.locate.text('Use License')
        self.locate.text('Restricted Uses')
        self.locate.text('Electronic Communication')
        self.locate.text('Your Account')
        self.locate.text('Reviews, Comments, and Other Material')
        self.locate.text('Legal Compliance')
        self.locate.text('Intellectual Property')
        self.locate.text('Revisions and Errata')
        self.locate.text('Disclaimer')
        self.locate.text('Links to Other Websites')
        self.locate.text('About Distributor and Provider')
        self.locate.text('Site Terms and Conditions Modifications')
        self.locate.text('Governing Law')
        self.locate.text('Indemnity')
        self.locate.text('General Terms')


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














