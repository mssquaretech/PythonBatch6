from selenium import webdriver
import unittest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class TOIndia_Testing(unittest.TestCase):

    def setUp(self):
        global TOI
        # opt = webdriver.ChromeOptions()
        # opt.add_argument("--disable-notifications")
        # TOI = webdriver.Chrome(options=opt)
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        TOI = webdriver.Chrome(desired_capabilities=caps)
        TOI.get("https://timesofindia.indiatimes.com/")
        TOI.maximize_window()

    def test_TOIndia(self):
        TOILinkXpath = "//a[@class='clickhere']"
        WebDriverWait(TOI, 10).until(EC.visibility_of_element_located((By.XPATH, TOILinkXpath)))
        TOILinkXpathElement = TOI.find_element_by_xpath(TOILinkXpath)
        TOILinkXpathElement.click()

        LatestnewsXpath = "//h4[contains(text(), 'The latest news')]"
        WebDriverWait(TOI, 100).until(EC.visibility_of_element_located((By.XPATH, LatestnewsXpath)))
        NotNowXpath = "//a[text()='Not Now']"
        NotNowXpathElement = TOI.find_element_by_xpath(NotNowXpath)
        NotNowXpathElement.click()

        ScrollXpath = "//button[text()='SUBMIT']"
        ScrollXpathElement = TOI.find_element_by_xpath(ScrollXpath)
        Poll = ActionChains(TOI)
        Poll.move_to_element(ScrollXpathElement).perform()

        PollOption = "//label[@for='83094094_1']/child::input"
        PollOptionXpath = TOI.find_element_by_xpath(PollOption)
        PollOptionXpath.click()
        time.sleep(2)
        ScrollXpathElement.click()

        NavBharatScoll = "//div[@class='_2JBqY']/following-sibling::span[@class='_2Pesn']"
        NavBharatScollElement = TOI.find_element_by_xpath(NavBharatScoll)
        NBnews = ActionChains(TOI)
        NBnews.move_to_element(NavBharatScollElement).perform()

        NavBharatFrame = "//iframe[contains(@title,'Navbharat')]"
        TOI.switch_to.frame(TOI.find_element_by_xpath(NavBharatFrame))

        NavBharatTotalNews = "(//span[@id='dotsblk']/descendant::li)"
        NavBharatTotalNewsElement = len(TOI.find_elements_by_xpath(NavBharatTotalNews))

        for a in range(NavBharatTotalNewsElement):
            a += 1
            NewsXpath = "(//span[@id='dotsblk']/descendant::li/child::a)["
            NewsXpath += str(a)
            NewsXpath += "]"

            WebDriverWait(TOI, 5).until(EC.element_to_be_clickable((By.XPATH, NewsXpath)))
            NewsClickXpathElement = TOI.find_element_by_xpath(NewsXpath)
            NewsClickXpathElement.click()

        TOI.switch_to.default_content()

        WebDriverWait(TOI, 100).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@title='Prime Blocker']")))
        TOI.switch_to.frame(TOI.find_element_by_xpath("//iframe[@title='Prime Blocker']"))
        ClosebuttonXpath = "//span[@class='close_ad_free']"
        time.sleep(2)
        ClosebuttonXpathElement = TOI.find_element_by_xpath(ClosebuttonXpath)
        ClosebuttonXpathElement.click()
        TOI.switch_to.default_content()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
