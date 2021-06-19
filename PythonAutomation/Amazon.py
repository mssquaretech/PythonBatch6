from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest

class AmazonDropDownSelect(unittest.TestCase):
    def setUp(self):
        global AmazonSelect
        AmazonSelect = webdriver.Chrome()
        AmazonSelect.get("https://www.amazon.in/")
        AmazonSelect.maximize_window()

    def test_AmazonSelect(self):
        TotalDropDownXpath = "(//select[@id='searchDropdownBox']/option)"
        TotalDropDown = len(AmazonSelect.find_elements_by_xpath(TotalDropDownXpath))
        print("Total Drop down options are: {}".format(TotalDropDown))

        for a in range(TotalDropDown):
            a += 1
            OptionXpath = "//select[@id='searchDropdownBox']/option["
            OptionXpath += str(a)
            OptionXpath += "]"

            AttributeValue = AmazonSelect.find_element_by_xpath(OptionXpath).get_attribute("value")

            selectDropDownXpath = "//select[@id='searchDropdownBox']"
            selectDropDownElement = AmazonSelect.find_element_by_xpath(selectDropDownXpath)

            SelectDropDown = Select(selectDropDownElement)
            SelectDropDown.select_by_value(AttributeValue)

unittest.main()