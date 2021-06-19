from selenium import webdriver
import unittest
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TimesofIndia(unittest.TestCase):

    def setUp(self):
        global driver
        # caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = "none"
        # driver = webdriver.Chrome(desired_capabilities=caps)

        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=opt)

        #driver = webdriver.Chrome()
        driver.get("https://timesofindia.indiatimes.com")
        driver.maximize_window()
        driver.implicitly_wait(20)

    def test_timesofindia(self):


        time.sleep(40)

        # mainpopupXpath = "//a[text()='Not Now']"
        # mainpopupXpathElement = driver.find_elements_by_xpath(mainpopupXpath)
        # for popup in (mainpopupXpathElement):
        #     if popup == mainpopupXpathElement:
        #         mainpopupXpathElement.click()
        #     else:
        #         pass

        WebDriverWait(driver, 140).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@title='Prime Blocker']")))
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Prime Blocker']"))

        adsXpath = "//span[@class='close_ad_free']"
        adsXpathElement = driver.find_element_by_xpath(adsXpath)
        adsXpathElement.click()
        driver.switch_to.default_content()

        pollXpath = "//div[text()='Poll']"
        pollXpathelement = driver.find_elements_by_xpath(pollXpath)
        action = ActionChains(driver)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pollXpathelement)))
        action.move_to_element(driver.find_element_by_xpath("//button[text()='SUBMIT']")).perform()

        #//div[@class='WcI8V']/div[text()='Poll']

        pollValueXpath = "//div[@class='_26fds']/descendant::input[@value='Agree']"
        pollValueXpathElement = driver.find_element_by_xpath(pollValueXpath)
        pollValueXpathElement.click()

        submitXpath = "//button[text()='SUBMIT']"
        submitXpathelement = driver.find_element_by_xpath(submitXpath)
        submitXpathelement.click()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Navbharat Times']"))
        #action = ActionChains(driver)
        #action.move_to_element(driver.find_element_by_xpath("//span/a[text()='Navbharat Times']"))
        time.sleep(3)

        newsoptionXpath = "//span[@id='dotsblk']/descendant::a"
        newsoptionXpathElement = driver.find_elements_by_xpath(newsoptionXpath)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, newsoptionXpath)))

        count = len(newsoptionXpathElement)

        #newschose = driver.find_element_by_xpath("//span[@id='dotsblk']/descendant::a")

        # for i in newsoptionXpathElement:
        #     if i == newschose:
        #         newsoptionXpathElement[i].click()

        for sites in newsoptionXpathElement:
            sites.click()

unittest.main()