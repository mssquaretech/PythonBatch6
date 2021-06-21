from selenium import webdriver
import time
import unittest
from selenium.webdriver import ActionChains

class test_MagicBrick(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.magicbricks.com/")
        driver.maximize_window()

    def test_magicB(self):

        scrollXpath = "//span[contains(text(),'Explore')]"
        scrollElement = driver.find_element_by_xpath(scrollXpath)
        time.sleep(3)

        action = ActionChains(driver)
        action.move_to_element(scrollElement).perform()

        exXpath = "//a[@id='postedByOwnersLink']"
        exElement = driver.find_element_by_xpath(exXpath)
        exElement.click()

        time.sleep(2)

        AllwindowsHandleList = driver.window_handles
        driver.switch_to.window(AllwindowsHandleList[1])

        windowXpath = "//span[@class='m-srp-card__title']"
        windowElement = driver.find_elements_by_xpath(windowXpath)

        for screen in windowElement:
            screen.click()

        newWindowList = driver.window_handles
        driver.switch_to.window(newWindowList[5])

    def tearDown(self):
        time.sleep(10)
        driver.quit()

unittest.main()