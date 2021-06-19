import time

from selenium import webdriver
import unittest

class Magicbricks(unittest.TestCase):

    def setUp(self) :
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.magicbricks.com/")
        driver.maximize_window()

    def test_magicprojects(self):
        print(driver.title)
        driver.switch_to.alert.accept()
        # projectpath = "//a[@id='postedByOwnersLink']"
        # projectpathxpath = driver.find_element_by_xpath(projectpath)
        # projectpathxpath.click()
        #
        # windownum = driver.window_handles
        # driver.switch_to.window(windownum[1])
        #
        # ownerproplinkelement =driver.find_elements_by_xpath("//span[@class='m-srp-card__title']")
        #
        # for ownerlink in ownerproplinkelement:
        #     ownerlink.click()
        #
        # ownerwindows = driver.window_handles
        # driver.switch_to.window(ownerwindows[4])


unittest.main()