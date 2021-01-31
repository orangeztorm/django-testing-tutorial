import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from budget.models import Project
from django.urls import reverse


class TestProjectListPage(StaticLiveServerTestCase):

    def setup(self):
        self.browser = webdriver.Chrome('functional_test/chromedriver.exe')

    def tearDown(self):
        self.browser = webdriver.Chrome('functional_test/chromedriver.exe')
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser = webdriver.Chrome('functional_test/chromedriver.exe')
        self.browser.get(self.live_server_url)
        time.sleep(20)
