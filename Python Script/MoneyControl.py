from selenium import webdriver
from selenium.webdriver import ActionChains

import unittest
import time

class Moneycontrol(unittest.TestCase):

    def test_Searchline(self):
        driver = webdriver.Chrome()
        driver.get("https://www.moneycontrol.com")
        TopSearch = "//form[@name='form_topsearch']/input[@id='search_str']"

        TopSearchElement = driver.find_element_by_xpath(TopSearch)
        TopSearchElement.send_keys("RIL")

        time.sleep(2)

        InputSearch = "//div[@class='top_asugscrl']/ul[contains(@class,'scrollBar')]/li[1]/a"
        InputElement = driver.find_element_by_xpath(InputSearch)
        InputElement.click()

        RilValuePath = "//input[@id='nsespotval']"
        RilValueElement = driver.find_element_by_xpath(RilValuePath)

        print(RilValueElement.get_attribute('value'))

        time.sleep(3)

        ScrollToVariable = "//table[@class='frevdat']/tbody//td[text()='OperatingProfit']"
        ScrollElement = driver.find_element_by_xpath(ScrollToVariable)

        action = ActionChains(driver)
        action.move_to_element(ScrollElement).perform()
        time.sleep(10)


unittest.main()
