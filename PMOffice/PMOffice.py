from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class test_PMOffice(unittest.TestCase):

    def setUp(self):
        global driver

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome(desired_capabilities=caps)

        driver = webdriver.Chrome()
        driver.get("https://www.pmindia.gov.in/en")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_PMO(self):

        scrollXpath = "//span[starts-with(text(),'Government')]"
        scrollElement = driver.find_element_by_xpath(scrollXpath)

        actions = ActionChains(driver)
        actions.move_to_element(scrollElement).perform()

        windowXpath = "//ul[@class='our-gov clearfix']/descendant::a[@target='_blank']"
        windowElement = driver.find_elements_by_xpath(windowXpath)

        for clickWin in windowElement:
            clickWin.click()

        AllwindowHandlelist = driver.window_handles
        driver.switch_to.window(AllwindowHandlelist[7])

        scrolLokXpath = "//a[@title='India Map']"
        scrolLokElement = driver.find_element_by_xpath(scrolLokXpath)

        actions = ActionChains(driver)
        actions.move_to_element(scrolLokElement).perform()

        profileXpath = "//a[@title='Profile']"
        profileElement = driver.find_element_by_xpath(profileXpath)
        profileElement.click()

        AllwindowHandlelist1 = driver.window_handles
        driver.switch_to.window(AllwindowHandlelist1[10])

        formerXpath = "//img[@alt='Former Speaker']"
        formerElement= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, formerXpath)))

        formerElement.click()

        speakerNameXpath = "//a[contains(@href,'former')]"
        speakerNameElement = driver.find_elements_by_xpath(speakerNameXpath)

        for names in speakerNameElement:

            if names.text != "":
                print(names.text)
            else:
                continue

    # def tearDown(self):
unittest.main()