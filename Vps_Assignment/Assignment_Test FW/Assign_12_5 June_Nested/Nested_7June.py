import time

from selenium import webdriver

import unittest

from selenium.webdriver import ActionChains


class test_nestedframe(unittest.TestCase):
    def setUp(self):

        global Nested
        opt = webdriver.ChromeOptions()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        Nested = webdriver.Chrome(options=opt)
        Nested.get("https://www.hotfrog.com/")
        Nested.maximize_window()
        Nested.implicitly_wait(10)

    def test_nestedpage(self):


        Nested.switch_to.frame(Nested.find_element_by_id("aswift_1"))

        adheadingXpath = "//div[contains(@class,'title')]"
        adheadingXpathElement = Nested.find_element_by_xpath(adheadingXpath)
        print(adheadingXpathElement.text)
        #Nested.switch_to.default_content()


        Nested.switch_to.frame(Nested.find_element_by_xpath("//html[@lang='en']/body/iframe"))

        NewframXpath = "//html/descendant::script"
        NewframXpathelement = Nested.find_element_by_xpath(NewframXpath).get_attribute("src")

        print(NewframXpathelement)
        Nested.get(NewframXpathelement)

        #textXpath = "//body/pre"
        textXpathelement = Nested.find_element_by_xpath("//body/pre")
        #print(textXpathelement.text)

        res = textXpathelement.text
        print("The Count is:", res.count("this"))


unittest.main()
