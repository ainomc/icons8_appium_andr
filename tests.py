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
        self.locate.locate_xpath(menu_toggle)
        self.locate.locate_part_text('Free Flat Icons')
        self.locate.locate_xpath(search_field)
        self.locate.locate_part_text('Most Popular')
        self.locate.locate_part_text('View all...')
        self.locate.locate_xpath(first_category_icon)
        self.locate.locate_xpath(first_landing_colors)
        self.locate.locate_part_text('For iOS, Windows, and Android')
        self.locate.locate_xpath(first_search_type)

    def test_homepage_ui_items_2(self, open_url):
        """Check home page ui presents"""
        self.locate.locate_part_text('Features for UI Designers and Developers')
        self.locate.locate_part_text('Single Style')
        self.locate.locate_part_text('Editable Vectors')
        self.locate.locate_part_text('Fonts Generator')
        self.locate.locate_part_text('Icon Recoloring')
        self.locate.locate_part_text('Mac&Win Apps')
        self.locate.locate_part_text('HTML Embedding')
        self.locate.locate_xpath(icon9_video)
        self.locate.locate_part_text('Daily Updates Guided by Your Ideas')

    def test_homepage_ui_items_3(self, open_url):
        """Check home page ui presents"""
        self.locate.locate_part_text('Free Apps for the Web, Mac, and Windows')
        self.click.click_text('Mac')
        self.locate.locate_xpath(free_app_mac_bar)
        self.click.click_text('Windows')
        self.locate.locate_xpath(free_app_win_bar)
        self.locate.locate_text('Download')
        self.locate.locate_xpath(free_app_win_bar)
        self.locate.locate_xpath(first_company_in_bar)
        self.locate.locate_part_text('The Community Loves Icons8')
        self.locate.locate_part_text('Pinterest')
        self.locate.locate_part_text('Icons by Category')
        self.locate.locate_part_text('Social Media Icons')

    def test_footer_about(self, open_url):
        """Check About module in home page footer"""
        self.locate.locate_text('About')
        self.locate.locate_text('Business Model')
        self.locate.locate_text('Team')
        self.locate.locate_text('Our Open Source Projects')

    def test_footer_Ideas_for_Icons_popular(self, open_url):
        """Check Popular button in home page footer"""
        self.locate.locate_text('Ideas for Icons')
        self.click.click_text('Popular')
        self.locate.locate_text('Request Icons')

    def test_footer_Ideas_for_Icons_new(self, open_url):
        """Check New button in home page footer"""
        self.click.click_text('New')
        self.locate.locate_text('Request Icons')

    def test_footer_Ideas_for_Icons_submit(self, open_url):
        """Check Submit button in home page footer"""
        self.click.click_text('Submit')
        self.locate.locate_text('Request Icons')

    def test_footer_support_faq(self, open_url):
        """Check FAQ button in home page footer"""
        self.locate.locate_text('Support')
        self.click.click_text('FAQ')
        self.locate.locate_text('Advice and answers from the Icons8 Team')

    def test_footer_support_contact_us(self, open_url):
        """Check Contact us button in home page footer"""
        self.click.click_text('Contact us')
        self.locate.locate_text('Contact Icons8')

    def test_footer_news_and_social_medium(self, open_url):
        """Check Medium button in home page footer"""
        self.locate.locate_text('News and Social')
        self.locate.locate_text('Blog')
        self.click.click_part_text('Medium')
        self.locate.locate_text('ICONOGRAPHY')

    def test_footer_licenses_free_license(self, open_url):
        """"Check Free Licenses button in home page footer"""
        self.locate.locate_text('Licenses')
        self.click.click_text('Free License')
        self.locate.locate_part_text('Use Icons for Free')
        self.locate.locate_part_text('Why to Link?')
        self.locate.locate_part_text('Where to Put the Link?')
        self.locate.locate_part_text('Websites')
        self.locate.locate_part_text('Desktop Apps')
        self.locate.locate_part_text('Mobile Apps')
        self.locate.locate_part_text('Open Source')

    def test_footer_licenses_buy_full_license(self, open_url):
        """Check Full License button in home page footer"""
        self.click.click_text('Buy Full License')
        self.locate.locate_part_text('Paid or Free, You Are Our Hero!')
        self.locate.locate_part_text('Unlimited Plan')
        self.locate.locate_part_text('Free')
        self.locate.locate_part_text('Service Integration')
        self.locate.locate_part_text('Paid License Summary')
        self.locate.locate_part_text('Permitted Uses')
        self.locate.locate_part_text('Prohibited Uses for all Licenses')
        self.locate.locate_part_text("What's Included")
        self.locate.locate_part_text("Built-in Editing Tools")

    def test_footer_developers_github(self, open_url):
        """Check GitHub button in home page footer"""
        self.locate.locate_text('Developers')
        self.locate.locate_part_text('Free Icons for Open Source')
        self.click.click_text('GitHub')
        self.locate.locate_part_text('Repositories')

    def test_footer_developers_api(self, open_url):
        """Check API button in home page footer"""
        self.click.click_text('API')
        self.locate.locate_part_text('Icons8 API allows us to search and obtain')

    def test_footer_privacy_policy(self, open_url):
        """Check Privacy Policy button in home page footer"""
        self.click.click_text('Privacy Policy')
        self.locate.locate_part_text('Our Privacy Policy was last updated')
        self.locate.locate_text('Your Privacy')
        self.locate.locate_text('Definitions')
        self.locate.locate_text('Information We Collect')
        self.locate.locate_text('Computer Information Collected')
        self.locate.locate_text('How We Use Your Information')
        self.locate.locate_text('Opt-Out')
        self.locate.locate_text('Links to Other Websites')
        self.locate.locate_text('Security')
        self.locate.locate_text('Privacy Policy Updates')
        self.locate.locate_part_text('Questions About Our Privacy Practices')

    def test_footer_terms_and_conditions(self, open_url):
        """Check Terms and Conditions button in home page footer"""
        self.click.click_text('Terms and Conditions')
        self.locate.locate_part_text('This web page represents a legal document')
        self.locate.locate_text('Definitions')
        self.locate.locate_text('Use License')
        self.locate.locate_text('Restricted Uses')
        self.locate.locate_text('Electronic Communication')
        self.locate.locate_text('Your Account')
        self.locate.locate_text('Reviews, Comments, and Other Material')
        self.locate.locate_text('Legal Compliance')
        self.locate.locate_text('Intellectual Property')
        self.locate.locate_text('Revisions and Errata')
        self.locate.locate_text('Disclaimer')
        self.locate.locate_text('Links to Other Websites')
        self.locate.locate_text('About Distributor and Provider')
        self.locate.locate_text('Site Terms and Conditions Modifications')
        self.locate.locate_text('Governing Law')
        self.locate.locate_text('Indemnity')
        self.locate.locate_text('General Terms')


class TestMainMenu(ContextMain):
    """Main menu tests class"""

    def test_open_Icons_from_menu(self, open_menu_toggle):
        """Open Icons from left side menu"""
        self.click.click_text('Icons')
        self.locate.locate_text("New Icons")

    def test_open_Request_from_menu(self, open_menu_toggle):
        """Open Request from left side menu"""
        self.click.click_text('Request')
        self.locate.locate_text("Request Icons")
        
    def test_open_Buy_from_menu(self, open_menu_toggle):
        """Open Buy from left side menu"""
        self.click.click_text('Buy')
        self.locate.locate_text("Paid or Free, You Are Our Hero!")

    def test_presents_imassage_stickers_in_menu(self, open_menu_toggle):
        """Open Search from left side menu"""
        self.locate.locate_text('iMessage Stickers')

    def test_open_Icon_Search_AI_from_menu(self, open_menu_toggle):
        """Open Search from left side menu"""
        self.click.click_text('Icon Search AI')
        self.locate.locate_text("Draw an icon (Rough is OK):")

    def test_open_Blog_from_menu(self, open_menu_toggle):
        """Open Blog from left side menu"""
        self.click.click_text('Blog')
        self.locate.locate_xpath(blog_list_news)

    def test_open_Register_from_menu(self, open_menu_toggle):
        """Open Register from left side menu"""
        self.click.click_part_text('Register')
        self.locate.locate_part_text('Register at Icons8')

    def test_open_Login_from_menu(self, open_menu_toggle):
        """Open Login from left side menu"""
        self.click.click_part_text('Login')
        self.locate.locate_text('Login to Icons8')
        
    def test_open_lang_menu_from_menu(self, open_menu_toggle):
        """Open Language menu from left side menu"""
        self.click.click_xpath(lang_menu)
        self.locate.locate_part_text('Chinese')
        self.locate.locate_part_text('Spanish')
        self.locate.locate_part_text('Russian')
        self.locate.locate_part_text('German')


class TestIconsPage(ContextMain):
    """Icon Page tests class"""

    def test_presents_search_field(self, open_icons):
        """Check presents of search field"""
        self.locate.locate_xpath(icons_search_field)

    def test_presents_icons_filters(self, open_icons):
        """Check presents of icons filter"""
        self.locate.locate_xpath(icons_filter_1)
        self.locate.locate_xpath(icons_filter_2)
        self.locate.locate_xpath(icons_filter_3)

    def test_presents_icon_resuilt(self, open_icons):
        """Check presents of icon on the page"""
        self.locate.locate_xpath(icon_result)

    def test_presents_category_menu(self, open_icons):
        """Check presents of category menu"""
        self.click.click_xpath(category_menu)
        self.locate.locate_text('iOS 10')
        self.locate.locate_text('Adobe Design')


class TestRequestPage(ContextMain):
    """Request Page tests class"""


    def test_presents_fast_for_50(self, open_request):
        """Check "Fast for $50/icon" """
        self.click.click_text('Fast for $50/icon')
        self.locate.locate_text('How Fast Is It?')
        self.locate.locate_text('How Much Is It?')
        self.locate.locate_text('Where Do I Start?')

    def test_presents_hot_ideas(self, open_request):
        """Check Hot Ideas list"""
        self.locate.locate_text('Hot Ideas')
        self.locate.locate_xpath(idea)

    def test_presents_latest_ideas(self, open_request):
        """Check Hot Ideas list"""
        self.click.click_part_text('Latest Ideas')
        self.locate.locate_xpath(idea)

    def test_presents_popular_ideas(self, open_request):
        """Check Popular Ideas list"""
        self.click.click_part_text('Popular Ideas')
        self.locate.locate_xpath(idea)


class TestBuyPage(ContextMain):
    """Buy Page tests class"""


    def test_presents_unlimited_plan(self, open_buy):
        """Check presents of Unlimited Plan"""
        self.locate.locate_part_text('Unlimited Plan')
        self.locate.locate_part_text('Buy for $19.90/month')

    def test_presents_free_plan(self, open_buy):
        """Check presents of Free plan"""
        self.locate.locate_part_text('Free')
        self.locate.locate_part_text('Try for Free')

    def test_presents_service_integration_plan(self, open_buy):
        """Check presents of Service Integration plan"""
        self.locate.locate_part_text('Service Integration')
        self.locate.locate_part_text('Starting from $100/month')

    def test_presents_video_in_buy_page(self, open_buy):
        """Check presents of video on buy page"""
        self.locate.locate_xpath(video_in_buy_page)

    def test_presents_info_text_in_buy_page(self, open_buy):
        """Check presents of info text in buy page"""
        self.locate.locate_part_text('Paid License Summary')
        self.locate.locate_part_text('Standard License Agreement')
        self.locate.locate_part_text('Permitted Uses')
        self.locate.locate_part_text('Prohibited Uses for all Licenses')
        self.locate.locate_part_text("What's Included")
        self.locate.locate_part_text('All Plans Except PNG Cobra')
        self.locate.locate_part_text('New Icons and Support')
        self.locate.locate_part_text('Built-in Editing Tools')
        self.locate.locate_part_text('Web App')
        self.locate.locate_part_text('Icons8 App for Mac and Windows')
        self.locate.locate_part_text('FAQ on Icons8 App')














