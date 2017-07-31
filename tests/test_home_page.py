# -*- coding: utf-8 -*
"""Home page tests"""

from context.context_base import ContextMain
from locators.locators_base import *



class TestHomePage(ContextMain):
    """Home page tests"""

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