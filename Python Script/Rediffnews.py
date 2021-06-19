import time

from selenium import webdriver
import unittest


class Rediffnews(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.rediff.com/")
        driver.maximize_window()

    def test_newlist(self):

        newpath ="//li[@class='news']"
        newpathelement = driver.find_element_by_xpath(newpath)
        newpathelement.click()

        time.sleep(3)
        newlistpath = "//div[@class='newleftcontainer']//h2/a"
        newlistpathlist = driver.find_elements_by_xpath(newlistpath)

        for listnews in newlistpathlist:
            print(listnews.text)

unittest.main()