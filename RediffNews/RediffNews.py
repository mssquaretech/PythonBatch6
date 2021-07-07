import time
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains

class Rediff(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://rediff.com/")
        driver.maximize_window()

    def test_LoopTesting(self):

        time.sleep(5)
        scrollXpath = "//a[@class='backgetahead']"
        scrollElement = driver.find_element_by_xpath(scrollXpath)

        time.sleep(2)

        action = ActionChains(driver)
        action.move_to_element(scrollElement).perform()

        time.sleep(2)

        newsListXpath = "//div[@id='topdiv_0']"
        newsListElement = driver.find_elements_by_xpath(newsListXpath)

        for news in newsListElement:
            print(news.text)

    def tearDown(self):
        time.sleep(10)
        driver.quit()

unittest.main()