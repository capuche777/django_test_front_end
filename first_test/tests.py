from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class ChromeTest(LiveServerTestCase):

    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)

    def test_title(self):
        driver = self.driver
        driver.get('https://python.org')
        self.assertEquals('Welcome to Python.org', driver.title)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('https://python.org')
        elem = driver.find_element_by_name("q")
        elem.send_keys("django")
        elem.send_keys(Keys.RETURN)
        self.assertEquals("https://www.python.org/search/?q=django&submit=", driver.current_url)

    def tearDown(self):
        self.driver.quit()
