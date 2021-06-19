import time

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.support.select import Select


class PMsite(unittest.TestCase):

    def setUp(self):

        global driver
        caps = DesiredCapabilities.CHROME
        caps["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome(desired_capabilities = caps)
        driver.get("https://www.pmindia.gov.in/en/")
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_pmoweb(self):

        movetopage ="//span[text()='Government'][1]"
        movetopageElement = driver.find_element_by_xpath(movetopage)
        pagemove= ActionChains(driver)
        pagemove.move_to_element(movetopageElement).perform()


        govlink = "//div[@class='footer-mid-right']//li/a[@target='_blank']"
        govlinklist = driver.find_elements_by_xpath(govlink)

        for openlink in govlinklist:
            openlink.click()

        gotowindow = driver.window_handles
        driver.switch_to.window(gotowindow[7])

        profilepath = "//div[@class='profile']/ul/li[@class='first']"
        profilepathElement = driver.find_element_by_xpath(profilepath)
        action = ActionChains(driver)
        action.move_to_element(profilepathElement).perform()
        profilepathElement.click()

        newwindow = driver.window_handles
        driver.switch_to.window(newwindow[10])

        formarlink =  "//a/img[contains(@alt,'Former Speaker')]"
        formarlinkElement = driver.find_element_by_xpath(formarlink)
        formarlinkElement.click()

        formarname ="//a[contains(@href ,'former/')]"
        formarnamelist = driver.find_elements_by_xpath(formarname)

        for name in formarnamelist:
            if (name.text != ""):
                print(name.text)
            else:
                continue

unittest.main()