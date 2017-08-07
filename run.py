# -*- coding:utf-8 -*-

__author__ = "Zeal Zhang/zealzhangz@gmail.com"
__version__ = "0.0.1"

import unittest
import time
from CommonUtil import HTMLTestRunner
from Module.SubModule1 import SampleTest1
from Module.SubModule2 import SampleTest2
from CommonUtil.setttings import Settings

testunit = unittest.TestSuite()

# Cases
testunit.addTest(unittest.makeSuite(SampleTest1.SampleTestCase1))
testunit.addTest(unittest.makeSuite(SampleTest2.SampleTestCase2))

# Generate result file name
now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
fp = open("Result/Result-" + now + ".html", 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Github unit test',
    description='A sample of selenium test.Environment: %s ' % Settings.ENV
)
# Invoke TestRunner
runner.run(testunit)
fp.close()
