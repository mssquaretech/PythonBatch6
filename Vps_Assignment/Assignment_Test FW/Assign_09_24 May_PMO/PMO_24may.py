from selenium import webdriver
import unittest
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class test_Pmosite(unittest.TestCase):
    def setUp(self):
        global driver
        caps = DesiredCapabilities().CHROME
        caps["PageLoadStrategy"] = "none"
        driver = webdriver.Chrome(desired_capabilities=caps)

        #driver = webdriver.Chrome()
        driver.get("https://www.pmindia.gov.in/en/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_PmoPage(self):
        findwebpageXpath = "//ul[@class='our-gov clearfix']/li/a"
        findwebpageXpathelement = driver.find_elements_by_xpath(findwebpageXpath)
        count = len(findwebpageXpathelement)

        bannerXpath = "//ul[@class='our-gov clearfix']/li/a[@href='/en']"
        bannerXpathelem = driver.find_element_by_xpath(bannerXpath)

        #RemoveSiteXpath = bannerXpathelem.text
        #print(RemoveSiteXpath)

        for sites in findwebpageXpathelement:
              if sites == bannerXpathelem:
                  pass
              else:
                  sites.click()

        Allwindowlist = driver.window_handles
        driver.switch_to.window(Allwindowlist[7])


        #scrollLSXpath = "//div[@class='welcom']/h2"
        LoksabhaProfileXpath = "//ul/li[@class='first']/a[@title='Profile']"

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, LoksabhaProfileXpath)))

        LoksabhaProfileXpathElement = driver.find_element_by_xpath(LoksabhaProfileXpath)

        #Loksabhascroll = ActionChains(driver)
        #Loksabhascroll.move_to_element(LoksabhaProfileXpathElement).perform()

        LoksabhaProfileXpathElement.click()

        Newwindowlist = driver.window_handles
        driver.switch_to.window(Newwindowlist[10])

        FormerSpeakerXpath = "//a[@onmouseout='MM_swapImgRestore()']/img[@alt='Former Speaker']"
        FormerSpeakerXpathElement = driver.find_element_by_xpath(FormerSpeakerXpath)
        FormerSpeakerXpathElement.click()

        SpeakernameXpath = "//tbody/tr/td[@valign='top']/a[contains(@href,'former')]"
        SpeakernameXpathElement = driver.find_elements_by_xpath(SpeakernameXpath)
        count = len(SpeakernameXpathElement)


        #FormerSpeakerelement = driver.find_element_by_xpath("//tbody/tr/td[@valign='top']/a[contains(@href,'former')]")

        for i in range(1, count):
             #Select(SpeakernameXpathElement).select_by_index(i)
             print(SpeakernameXpathElement[i].text)



unittest.main()