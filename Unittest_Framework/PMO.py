from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class PMO(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome(desired_capabilities=caps)
        driver.get("https://www.pmindia.gov.in/en/")
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_PMOtest(self):
        movetoXpath = "(//ul[@class = 'our-gov clearfix']//h4)[1]"
        moveToEle = driver.find_element_by_xpath(movetoXpath)

        action = ActionChains(driver)
        action.move_to_element(moveToEle).perform()

        listofWebsiteXpath = "//ul[@class = 'our-gov clearfix']/li/a[@target = '_blank']"
        websiteList = driver.find_elements_by_xpath(listofWebsiteXpath)

        for site in websiteList:
            site.click()

        allowWndowHandle = driver.window_handles
        driver.switch_to.window(allowWndowHandle[7])

        profileXpth = "//a[contains(text(),'Profile')]"
        # WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, profileXpth)))
        driver.find_element_by_xpath(profileXpth).click()

        allowWndowHandle = driver.window_handles
        driver.switch_to.window(allowWndowHandle[10])

        formerSpeakerXpath = "//a/img[@alt = 'Former Speaker']"
        formerSpeakerEle = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, formerSpeakerXpath)))
        formerSpeakerEle.click()

        nameXpaths = "//tr[@align = 'center']//a"
        nameLists = driver.find_elements_by_xpath(nameXpaths)

        for name in nameLists:
            if (name.text) != "":
                print(name.text)
            else:
                continue

unittest.main()

