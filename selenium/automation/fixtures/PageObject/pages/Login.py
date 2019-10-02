from fixtures.PageObject.Locator import Locator

class Login(object):
  def __init__(self, driver):
      self.driver = driver

      # locators definition
      self.usernameInput = driver.find_element_by_id(Locator.username_input)
      self.passwordInput = driver.find_element_by_id(Locator.password_input)
      self.loginButton  = driver.find_element_by_id(Locator.login_button)

  def getUsernameInput(self):
    return self.usernameInput

  def getPasswordInput(self):
    return self.passwordInput

  def getLoginButton(self):
    return self.loginButton
