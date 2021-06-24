from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest

class AmazonAllDropDown(unittest.TestCase):
    def setUp(self):
        global driver
        driver =  webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.maximize_window()

    def test_AmazonDropdown(self):
        ListallXpath = "//select[@name='url']/option"
        ListallElement = driver.find_elements_by_xpath(ListallXpath)

        # count = len(ListallElement)

        # selectElem = driver.find_element_by_xpath("//select[@name='url']")

        # for i in range(1,count):
        #     Select(selectElem).select_by_index(i)
        #     print(ListallElement[i].text)

        for opt in ListallElement:
            opt.click()
            print(opt.text)


    # def tearDown(self):
    #     driver.close()

unittest.main()
