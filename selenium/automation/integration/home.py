from selenium.webdriver.common.keys import Keys

from fixtures.TestBase.TestBase import TestBase
from fixtures.PageObject.pages.Home import Home
from settings import PAGES

class HomeTest(TestBase):

  def test_home_page(self):

# screenshot relative paths
    ss_path = 'home_page'
  
    driver = self.driver
    driver.get(PAGES['home'])
    self.assertIn("React App", driver.title)

    page = Home(driver)

    driver.implicitly_wait(10) # seconds

    self.take_screenshot()

    assert "No results found." not in driver.page_source
