from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest

class test_Loop(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://amazon.com")
        driver.maximize_window()

    def test_LoopTesting(self):
        listCategoryXpath = "//select[@name='url']/option"
        listCategoryList = driver.find_elements_by_xpath(listCategoryXpath)

        count = len(listCategoryList)

        # for bucket in listCategoryElement:
        #     bucket.click()
        #     print(bucket.text)

        elen = driver.find_element_by_xpath("//select[@name='url']")

        for i in range(1,count):
            Select(elen).select_by_index(i)
            print(listCategoryList[i].text)

unittest.main()