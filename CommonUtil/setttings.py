# -*- coding:utf-8 -*-

__author__ = "Zeal Zhang/zealzhangz@gmail.com"
__version__ = "0.0.1"


class Settings:
    # Environment
    ENV = "TEST"

    # Please do not test in production environment
    # Default login url
    LOGIN_URL = "https://github.com/login"

    # Your username
    USER_NAME = "yourusername"

    # Default password
    PASSWD = "yourpassword"

    # Wait seconds
    WAIT_SECONDS = 10

    # Browser web driver path
    WEB_DRIVER_PATH = "/yourwebdriverpath/chromedriver"

    # Constant Xpath string
    LOGOUT_BUTTON_XPATH = "//*[@id='user-links']/li[3]/div/div/form/button"

    # Start project [a] tag
    START_PROJECT_XPATH = "//*[@id='js-pjax-container']/div[1]/div/div/a[2]"

    # Subhead heading
    SUBHEAD_HEADING = "//*[@id='new_repository']/div[2]/h2"
