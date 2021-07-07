import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Draggable(unittest.TestCase):

    def setUp(self):
        global driver
        driver= webdriver.Chrome()
        driver.get("https://jqueryui.com/draggable/")
        driver.maximize_window()

    def test_Draggable(self):
        scrollXpath = "//a[@tabindex='0']"
        scrollElement = driver.find_element_by_xpath(scrollXpath)

        action= ActionChains(driver)
        action.move_to_element(scrollElement).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

        drag = "//div[@id='draggable']"
        dragElement = driver.find_element_by_xpath(drag)

        action = ActionChains(driver)
        action.drag_and_drop_by_offset(dragElement,250,118).perform()

        # driver.switch_to.default_content()

        # Below method without Drag and Drop
    def test_Draggable1(self):

        scrollXpath1 = "//a[@tabindex='0']"
        scrollElement1 = driver.find_element_by_xpath(scrollXpath1)

        action1 = ActionChains(driver)
        action1.move_to_element(scrollElement1).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

        time.sleep(2)
        SourceXpath = driver.find_element_by_xpath("//div[@id='draggable']")
        # TargetXpath = driver.find_element_by_xpath("//div[@style='position: relative; left: 307px; top: 199px;']")

        action1 = ActionChains(driver)
        # action.drag_and_drop().move_by_offset(307, 199).release().perform()
        action1.click_and_hold(SourceXpath).move_by_offset(220,290).release().perform()


    def tearDown(self):
        time.sleep(10)
        driver.close()

unittest.main()