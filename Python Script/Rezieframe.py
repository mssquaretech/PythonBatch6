from selenium import webdriver
from selenium.webdriver import ActionChains

import unittest

class Resizeframe(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/draggable/")

    def test_Resize(self):
        resizepath = "//a[contains(text(),'Resizable')]"
        resizepathelment = driver.find_element_by_xpath(resizepath)
        resizepathelment.click()

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[@tabindex='0']")).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
        extendlink = "//div[@id='resizable']/div[last()]"
        extendlinkElement = driver.find_element_by_xpath(extendlink)

        action = ActionChains(driver)
        action.click_and_hold(extendlinkElement).move_by_offset(100,100).release().perform()

unittest.main()