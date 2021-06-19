from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest

class NestedFrameTesting(unittest.TestCase):

    def setUp(self):
        global Nested
        opt = webdriver.ChromeOptions()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        Nested = webdriver.Chrome(options=opt)
        Nested.get("https://www.hotfrog.com/")
        Nested.maximize_window()
        Nested.implicitly_wait(10)

    def test_nestedframe(self):
        ScrollXpath = "//h2[text()='Recent Activity']"
        ScrollXpathElement = Nested.find_element_by_xpath(ScrollXpath)
        Action = ActionChains(Nested)
        Action.move_to_element(ScrollXpathElement).perform()

        FrameXpath = "//iframe[@id='aswift_1']"
        FrameXpathElement = Nested.find_element_by_xpath(FrameXpath)
        Nested.switch_to.frame(FrameXpathElement)

        Xpath = "//div[@id='mys-wrapper']/descendant::a[@dir='auto']"
        Value = Nested.find_element_by_xpath(Xpath)
        print("Available Ad present is: {}".format(Value.text))

        NextFrameXpath = "html[@lang='en']/child::body/child::iframe"
        NextFrameXpathElement = Nested.find_element_by_xpath(NextFrameXpath)
        Nested.switch_to.frame(NextFrameXpathElement)

        URL = Nested.find_element_by_xpath("//script").get_attribute("src")
        Nested.get(URL)

        TagxpathElement = Nested.find_element_by_xpath("//pre")
        WholeText = TagxpathElement.text

        Occurrence = WholeText.count("this")
        print("Total occurrence of 'this' keyword is: {}".format(Occurrence))

if __name__ == "__main__":
    unittest.main()