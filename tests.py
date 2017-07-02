# -*- coding: utf-8 -*
"""Main tests module"""

import time
from context import ContextMain
from locators import *

# python -m pytest -v tests.py -s

class TestMain(ContextMain):
    """Main tests class"""

    def test_homepage_ui_items_1(self):
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

    def test_homepage_ui_items_2(self):
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

    def test_homepage_ui_items_3(self):
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

    def test_footer_about(self):
        """Check About module in home page footer"""
        self.locate.locate_text('About')
        self.locate.locate_text('Business Model')
        self.locate.locate_text('Team')
        self.locate.locate_text('Our Open Source Projects')

    def test_footer_Ideas_for_Icons_popular(self):
        """Check Popular button in home page footer"""
        self.locate.locate_text('Ideas for Icons')
        self.click.click_text('Popular')
        self.locate.locate_text('Request Icons')

    def test_footer_Ideas_for_Icons_new(self):
        """Check New button in home page footer"""
        self.click.click_text('New')
        self.locate.locate_text('Request Icons')

    def test_footer_Ideas_for_Icons_submit(self):
        """Check Submit button in home page footer"""
        self.click.click_text('Submit')
        self.locate.locate_text('Request Icons')

    def test_footer_support_faq(self):
        """Check FAQ button in home page footer"""
        self.locate.locate_text('Support')
        self.click.click_text('FAQ')
        self.locate.locate_text('Advice and answers from the Icons8 Team')

    def test_footer_support_contact_us(self):
        """Check Contact us button in home page footer"""
        self.click.click_text('Contact us')
        self.locate.locate_text('Contact Icons8')

    def test_footer_news_and_social_medium(self):
        """Check Medium button in home page footer"""
        self.locate.locate_text('News and Social')
        self.locate.locate_text('Blog')
        self.click.click_part_text('Medium')
        self.locate.locate_text('ICONOGRAPHY')

    def test_footer_licenses_free_license(self):
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

    def test_footer_licenses_buy_full_license(self):
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

    def test_footer_developers_github(self):
        """Check GitHub button in home page footer"""
        self.locate.locate_text('Developers')
        self.locate.locate_part_text('Free Icons for Open Source')
        self.click.click_text('GitHub')
        self.locate.locate_part_text('Repositories')

    def test_footer_developers_api(self):
        """Check API button in home page footer"""
        self.click.click_text('API')
        self.locate.locate_part_text('Icons8 API allows us to search and obtain')

    def test_footer_privacy_policy(self):
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

    def test_footer_terms_and_conditions(self):
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




















