from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select

class TestingAmazon(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://amazon.in")
        driver.maximize_window()

    def test_SelectingValue(self):
        selectDropDownXpath = "//select[@name='url']"
        selectDropDownElement = driver.find_element_by_xpath(selectDropDownXpath)
        Select(selectDropDownElement).select_by_value("search-alias=mobile-apps")


    #def tearDown(self):
    #driver.close()

unittest.main()