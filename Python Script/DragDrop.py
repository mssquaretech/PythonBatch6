from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains

class DragDrop(unittest.TestCase):

    def setUp(self) :
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")

    def test_dragDrop(self):

        movepath = "//a[@tabindex='0']"
        movepathElement = driver.find_element_by_xpath(movepath)
        action = ActionChains(driver)
        action.move_to_element(movepathElement).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame']"))

        target = driver.find_element_by_xpath("//div[@id='draggable']")
        source = driver.find_element_by_xpath("//div[@id='droppable']")

        action = ActionChains(driver)
        action.drag_and_drop(source,target).perform()
        

unittest.main()
