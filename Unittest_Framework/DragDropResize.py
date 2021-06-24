from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains

class DragDropResize(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_DragDrop(self):

# Dropable
        dropablexpath = "//a[text() = 'Droppable']"
        dropableEle = driver.find_element_by_xpath(dropablexpath)
        dropableEle.click()

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[@tabindex = '0']")).perform()

        frameXpath = "//iframe[@class = 'demo-frame']"
        driver.switch_to.frame(driver.find_element_by_xpath(frameXpath))

        sourceEle = driver.find_element_by_id("draggable")
        targetEle = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(sourceEle,targetEle).perform()

        driver.switch_to.default_content()

# Draggable:
        draggablexpath = "//a[text() = 'Draggable']"
        draggableEle = driver.find_element_by_xpath(draggablexpath)
        draggableEle.click()

        moveEle = driver.find_element_by_class_name("view-source")
        action = ActionChains(driver)
        action.move_to_element(moveEle).perform()

        driver.switch_to.frame(driver.find_element_by_xpath(frameXpath))
        dragElement = driver.find_element_by_id("draggable")

        action = ActionChains(driver)
        action.drag_and_drop_by_offset(dragElement,150,120).perform()
        driver.switch_to.default_content()

# Resizable
        resizableXpath = "//a[text()= 'Resizable']"
        resizableEle = driver.find_element_by_xpath(resizableXpath)
        resizableEle.click()

        moveEle = driver.find_element_by_xpath("//a[text() = 'API documentation']")
        action = ActionChains(driver)
        action.move_to_element(moveEle).perform()

        driver.switch_to.frame(driver.find_element_by_class_name("demo-frame"))

        reSizeEle = driver.find_element_by_xpath("//div[@id = 'resizable']//div[last()]")
        action = ActionChains(driver)
        action.click_and_hold(reSizeEle).move_by_offset(120,200).release(reSizeEle).perform()

        driver.switch_to.default_content()

    # def tearDown(self):
    #     driver.close()

unittest.main()


