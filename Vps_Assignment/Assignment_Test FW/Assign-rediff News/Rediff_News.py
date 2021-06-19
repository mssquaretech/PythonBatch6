from selenium import webdriver
import unittest
import time

from selenium.webdriver.support.select import Select

class test_RediffNews(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.rediff.com/")
        driver.maximize_window()

    def test_Newspage(self):
        newsXpath = "(//a[@href='https://www.rediff.com/news'])[1]"
        newsXpathelement = driver.find_element_by_xpath(newsXpath)
        newsXpathelement.click()

        time.sleep(2)

        NewsResultXpath = "//div[@class='secstorybox news topboxheight relative']/h2"
        NewsResultXpathElement = driver.find_elements_by_xpath(NewsResultXpath)

        count = len(NewsResultXpathElement)

        for news in NewsResultXpathElement:
            print(news.text)


unittest.main()