# -*- coding:utf-8 -*-

__author__ = "Zeal Zhang/zealzhangz@gmail.com"
__version__ = "0.0.1"

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from CommonUtil.WebdriverUtil import ChromeWebdriver
from CommonUtil.setttings import Settings


class SampleTestCase2(unittest.TestCase, ChromeWebdriver):
    def __init__(self, *args, **kwargs):
        super(SampleTestCase2, self).__init__(*args, **kwargs)
        ChromeWebdriver.__init__(self)

    def setUp(self):
        # login
        self.login()

    def test_html_exist_string2(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Settings.START_PROJECT_XPATH))).click()
        test_is_present = self.wait.until(
            EC.text_to_be_present_in_element((By.XPATH, Settings.SUBHEAD_HEADING), "Create a new repository"))
        self.assertTrue(test_is_present)
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
