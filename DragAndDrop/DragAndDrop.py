import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Drag_And_Drop(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()

    def test_DragNDrop(self):
        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[@tabindex='0']")).perform()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

        SourceElement = driver.find_element_by_id("draggable")
        TargetElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(SourceElement,TargetElement).perform()

        driver.switch_to.default_content()
        driver.find_element_by_xpath("//a[text()='Resizable']").click()

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[@tabindex='0']")).perform()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

        resizeXpath = "//h3[text()='Resizable']/following-sibling::div[last()]"
        resizeElement = driver.find_element_by_xpath(resizeXpath)

        action = ActionChains(driver)
        action.click_and_hold(resizeElement).move_by_offset(100,100).release().perform()

    def tearDown(self):
        time.sleep(5)
        driver.quit()

unittest.main()

