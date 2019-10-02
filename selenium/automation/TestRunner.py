from unittest import TestLoader, TestSuite, TextTestRunner

from integration.login import LoginTest
from integration.home import HomeTest

if __name__ == "__main__":
    loader = TestLoader() 
    suite = TestSuite((
      loader.loadTestsFromTestCase(LoginTest),
      loader.loadTestsFromTestCase(HomeTest)
    ))

    runner = TextTestRunner(verbosity=3)
    runner.run(suite)