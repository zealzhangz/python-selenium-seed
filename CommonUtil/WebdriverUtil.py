# -*- coding:utf-8 -*-

__author__ = "Zeal Zhang/zealzhangz@gmail.com"
__version__ = "0.0.1"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setttings import Settings


class ChromeWebdriver(object):
    def __init__(self, env=Settings.ENV, loginUrl=Settings.LOGIN_URL, waitSeconds=Settings.WAIT_SECONDS,
                 driverPath=Settings.WEB_DRIVER_PATH):
        self.driverPath = driverPath
        self.driver = None
        self.env = env
        self.loginUrl = loginUrl
        self.wait = None
        self.waitSeconds = waitSeconds

    def login(self):
        self.driver = webdriver.Chrome(self.driverPath)
        self.wait = WebDriverWait(self.driver, self.waitSeconds)
        self.driver.get(self.loginUrl)
        phone = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login_field']")))
        passwd = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        loginbtn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login']/form/div[4]/input[3]")))

        phone.send_keys(Settings.USER_NAME)
        passwd.send_keys(Settings.PASSWD)
        loginbtn.send_keys(Keys.RETURN)

    def logout(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Settings.LOGOUT_BUTTON_XPATH))).click()


if __name__ == '__main__':
    test = ChromeWebdriver()
    test.login()
