from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest

class SelectClassTest(unittest.TestCase):

    def setUp(self):
        global SelectDrop
        SelectDrop = webdriver.Chrome()
        SelectDrop.get("https://www.amazon.in/")
        SelectDrop.maximize_window()

    def test_SelectDropDown(self):
        SelectDropDownXpath = "//select[@id='searchDropdownBox']"
        SelectDropDownElement = SelectDrop.find_element_by_xpath(SelectDropDownXpath)
        Select(SelectDropDownElement).select_by_value("search-alias=pantry")

    # def tearDown(self):
    #     SelectDrop.close()


unittest.main()