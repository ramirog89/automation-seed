from selenium.webdriver.common.keys import Keys

from fixtures.TestBase.TestBase import TestBase
from fixtures.PageObject.pages.Login import Login
from settings import PAGES

class LoginTest(TestBase):

  def test_login(self):

# screenshot relative paths
    ss_path = 'login_page'
  
    driver = self.driver
    driver.get(PAGES['login'])
    # self.assertIn("Python", driver.title)

    driver.implicitly_wait(10) # seconds


    # driver.header_overrides = {
    #     'New-Header1': 'Some Value',
    #     'New-Header2': 'Some Value'
    # }

    page = Login(driver)

    username = page.getUsernameInput()
    password = page.getPasswordInput()

    username.send_keys('admin')
    password.send_keys('password')

    self.take_screenshot()

    # assert que haya ido a la home.. y haya tirado un cartelito tambien

    page.getLoginButton().send_keys(Keys.RETURN)

    # for request in driver.requests:
    #   if request.response:
    #     print(
    #       request.path,
    #       request.response.status_code,
    #       request.response.headers['Content-Type']
    #     )

    assert "No results found." not in driver.page_source
