from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

import time

from selenium.webdriver.support.select import Select

class test_Bigbasket(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.bigbasket.com/ps/?q=Vegetables")
        driver.maximize_window()

    def test_Newspage(self):

        findfirstXpath = "//select[@id='sel1']/option"
        findfirstXpathelement = driver.find_elements_by_xpath(findfirstXpath)

        count = len(findfirstXpathelement)

        dropelement = driver.find_element_by_xpath("//select[@id='sel1']")

        for i in range(1, count):
            Select(dropelement).select_by_index(1)

        time.sleep(2)

        CheckGreenChilliXpath = "//a[@uib-tooltip='Chilli - Green, Organically Grown']"
        CheckGreenChilliXpathelement = driver.find_element_by_xpath(CheckGreenChilliXpath)

        action = ActionChains(driver)
        action.move_to_element(CheckGreenChilliXpathelement).perform()



        findGreenchilliXpath = "//a[@uib-tooltip='Chilli - Green, Organically Grown']/parent::div/following-sibling::div[@class='col-sm-12 col-xs-7 qnty-selection']/descendant::span/button/i"
        findGreenchilliXpathElement = driver.find_element_by_xpath(findGreenchilliXpath)
        findGreenchilliXpathElement.click()
        time.sleep(2)


        selectQtyXpath = "//a[@uib-tooltip='Chilli - Green, Organically Grown']/parent::div/following-sibling::div[@class='col-sm-12 col-xs-7 qnty-selection']/descendant::span/ul//descendant::span[text()='250 g']"
        selectQtyXpathelement = driver.find_element_by_xpath(selectQtyXpath)
        selectQtyXpathelement.click()
        time.sleep(2)

        addvegXpath = "//a[@uib-tooltip='Chilli - Green, Organically Grown']/parent::div/following-sibling::div[@class='col-sm-12 col-xs-12 add-bskt']/div//div[@class='delivery-opt']/div[@class='col-xs-12 bskt-opt ng-scope']/descendant::button[@qa='add']"
        addvegXpathElement = driver.find_element_by_xpath(addvegXpath)
        addvegXpathElement.click()





unittest.main()