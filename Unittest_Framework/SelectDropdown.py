from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select

class TestingAmazon(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()

    def test_SelectDropdown(self):
        dropDownXpath = "//select[@name='url']"
        dropDownELE = driver.find_element_by_xpath(dropDownXpath)
        # sel = Select(dropDownELE)
        Select(dropDownELE).select_by_value("search-alias=appliances")

        driver.find_element_by_xpath("//option[text()='Baby']").click()

    # def tearDown(self):
    #     driver.close()

unittest.main()



