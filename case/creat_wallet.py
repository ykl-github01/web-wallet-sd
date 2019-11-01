#coding=utf-8
from selenium import webdriver
import time
import os
'''
the class is for creat wallet
'''
class CreatWallet():
    def creat_wallet(self):
        #Set the file download address and format
        dir = os.path.abspath('..')
        url = dir + "\\downloadfile\\"
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir',url)
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/json')
        #Create a browser driver
        driver = webdriver.Firefox(firefox_profile=profile)
        #Enter the homepage
        driver.get('https://wallet.trias.one/')
        time.sleep(3)
        #Click create wallet
        driver.find_element_by_xpath('/html/body/div/div/main/div/a[1]/div[1]').click()
        driver.implicitly_wait(2)
        #Enter password and click ok to create
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/article[1]/section/div[2]/input').send_keys('123456789')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div/article[1]/section/a').click()
        time.sleep(4)
        #Click to download the file and confirm that it has been downloaded
        driver.find_element_by_xpath('/html/body/div/div/main/div/div/article[2]/section/a/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div/div/main/div/div/article[2]/section/p/a').click()
        time.sleep(1)
        driver.quit()