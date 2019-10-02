automation - selenium
===================
Working example of e2e testing with [python-selenium](https://selenium-python.readthedocs.io/)

## Requirements
* You should have [virtualenv](http://www.virtualenv.org/en/latest/#installation) installed. 
* You should have [pip](https://pypi.org/project/pip/) installed.
* You should have at least one driver available.
* * [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* * [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* * [Firefox](https://github.com/mozilla/geckodriver/releases)
* * [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
* If you are running on linux, make sure the driver in use is available in /usr/local/bin/{driver}

## Scaffolding
* automation (folder) `automation code`
* * fixtures (folder) `selenium assets`
* * * PageObject (folder) `page definitions`
* * * * pages (folder) `page object files`
* * * * Locator.py (file) `selenium selectors`
* * * TestBase (folder) `base definitions`
* * * * TestBase.py (file) `setup/teardown/webdriver instance`
* * * integration (folder) `functional tests`
* * * screenshots (folder) `screenshots`
* * settings.py (file) `settings DOMAIN/PAGES endpoints`
* * TestRunner.py (file) `register test cases and run in suite`
* drivers (folder) `drivers holder firefox/chrome/etc`

## Install
Clone this repo, set up and activate a virtualenv:
```console
git clone git@github.com:ramirog89/automation-seed.git
cd automation-seed/selenium
virtualenv env
source env/bin/activate
```

Setup dependencies:
```console
make install
```

### Setup driver
* Edit the `fixtures/TestBase/TestBase.py` file and set the webdriver you chose in setup

```console
// code
class TestBase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
// code
```

### Before run
* Make sure the FrontEnd and the Backend you're testing are running.
* Edit `settings.py` DOMAIN is target to your application

## Run e2e test
```console
make e2e
```
