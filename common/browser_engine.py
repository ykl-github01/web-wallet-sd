#coding=utf-8
from selenium import webdriver
import configparser
import sys, os


class Browser(object):

    # Open the browser
    def open_browser(self):
        config = configparser.ConfigParser()
        config.read("../config/config.ini", encoding='UTF-8')
        browser = config.get("browserType", "browserName")
        if browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "IE":
            self.driver = webdriver.Ie()
        #self.driver.set_window_size(1920, 1080)  # 分辨率
        #self.driver.maximize_window()
        #self.driver.get(url)
        return self.driver

        # Open url site

    def open_url(self, url):
        self.driver.get(url)

        # Close the browser

    def quit_browser(self):
        self.driver.quit()

    # Browser forward operation
    def forward(self):
        self.driver.forward()

    # Browser back action
    def back(self):
        self.driver.back()

    # An implicit wait
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
