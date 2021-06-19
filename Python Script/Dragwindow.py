from selenium import webdriver
from selenium.webdriver import ActionChains

import unittest

class Dragwindow(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/draggable/")
        driver.maximize_window()

    def test_dragWindow(self):
        dragpath = "//a[contains(text(),'Draggable')]"
        driver.find_element_by_xpath(dragpath).click()

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[@tabindex='0']")).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))
        dragvalue = "//div[@id='draggable']"
        dragvalueElement = driver.find_element_by_xpath(dragvalue)

        action = ActionChains(driver)
        action.drag_and_drop_by_offset(dragvalueElement,200,200).perform()

unittest.main()