from selenium import webdriver
import unittest

class Rediff(unittest.TestCase):
    def setUp(self):
        global driver
        driver =  webdriver.Chrome()
        driver.get("https://www.rediff.com/")
        driver.maximize_window()

    def test_RediffNews(self):
        driver.find_element_by_xpath("//li[@class = 'news']").click()
        newsListXpth = "//div[@class = 'secstorybox news topboxheight relative']//h2"
        newsEleList = driver.find_elements_by_xpath(newsListXpth)

        for news in newsEleList:
            print(news.text)

    # def tearDown(self):
    #     driver.close()

unittest.main()




