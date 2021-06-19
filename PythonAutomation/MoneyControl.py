from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import unittest

class MoneyControlTest(unittest.TestCase):
    def test_ScrollCheck(self):
        Mcontrol = webdriver.Chrome()
        Mcontrol.get("https://www.moneycontrol.com/")

        Searchbox = "//form[@id='form_topsearch']/child::input[@id='search_str']"
        SearchboxElement = Mcontrol.find_element_by_xpath(Searchbox)
        SearchboxElement.send_keys("RIL")
        time.sleep(3)

        Suggestion = "//div[@class='top_asugscrl']/descendant::a[starts-with(text(),'Reliance Industries')]/span"
        SuggestElement = Mcontrol.find_element_by_xpath(Suggestion)
        SuggestElement.click()

        NSEpath = "//div[@class='inprice1 nsecp']"
        NSEvalue = Mcontrol.find_element_by_xpath(NSEpath).get_attribute("data-numberanimate-value")
        print("Current NSE of RIL is: " + NSEvalue)

        Revenuepath = "//td[text()='Revenue']"
        RevenueElement = Mcontrol.find_element_by_xpath(Revenuepath)

        ActionObj = ActionChains(Mcontrol)
        ActionObj.move_to_element(RevenueElement).perform()

unittest.main()