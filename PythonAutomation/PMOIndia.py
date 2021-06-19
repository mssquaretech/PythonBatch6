from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class PMOTesting(unittest.TestCase):

    def setUp(self):
        global PMOIndia
        Caps = DesiredCapabilities().CHROME
        Caps["pageLoadStrategy"] = "none"
        PMOIndia = webdriver.Chrome(desired_capabilities=Caps)

        PMOIndia.get("https://www.pmindia.gov.in/en/")
        PMOIndia.maximize_window()

    def test_PMOTesting(self):
        VisibleLink = "//ul[@class='our-gov clearfix']/child::li/a"
        WebDriverWait(PMOIndia, 10).until(EC.element_to_be_clickable((By.XPATH, VisibleLink)))

        TotalLinksXpath = "(//ul[@class='our-gov clearfix']/child::li/a)"
        TotalLinksCount = len(PMOIndia.find_elements_by_xpath(TotalLinksXpath))

        for a in range(TotalLinksCount):
            a += 1
            LinkXpath = "(//ul[@class='our-gov clearfix']/descendant::i)["
            LinkXpath += str(a)
            LinkXpath += "]"

            if a == 7:
                pass
            else:
                PMOIndia.find_element_by_xpath(LinkXpath).click()

        ListofLinks = PMOIndia.window_handles
        PMOIndia.switch_to.window(ListofLinks[7])

        ScrollXpath = "//div[@class='findRepresn']"

        WebDriverWait(PMOIndia, 10).until(EC.visibility_of_element_located((By.XPATH, ScrollXpath)))

        ScrollElement = PMOIndia.find_element_by_xpath(ScrollXpath)

        ScrollImage = ActionChains(PMOIndia)
        ScrollImage.move_to_element(ScrollElement).perform()

        ProfileClickXpath = "//a[@title='Profile']"
        ProfileClickElement = PMOIndia.find_element_by_xpath(ProfileClickXpath)
        ProfileClickElement.click()

        NewSpeakerLink = PMOIndia.window_handles
        PMOIndia.switch_to.window(NewSpeakerLink[10])

        FormerSpeakerXpath = "//a[@href='frmspeaker.asp']/child::img"

        WebDriverWait(PMOIndia, 10).until(EC.element_to_be_clickable((By.XPATH, FormerSpeakerXpath)))

        ClickElement = PMOIndia.find_element_by_xpath(FormerSpeakerXpath)
        ClickElement.click()

        SpeakerVisible = "//td[@valign='top']/a"

        WebDriverWait(PMOIndia, 10).until(EC.visibility_of_element_located((By.XPATH, SpeakerVisible)))

        SpeakerCountXpath = "(//td[@valign='top']/a)"
        TotalFormerSpeaker = len(PMOIndia.find_elements_by_xpath(SpeakerCountXpath))
        print("Below are the Former Speakers of India:")

        for x in range(TotalFormerSpeaker):
            x += 1
            SpeakerXpath = "(//td[@valign='top']/a)["
            SpeakerXpath += str(x)
            SpeakerXpath += "]"

            SpeakerName = PMOIndia.find_element_by_xpath(SpeakerXpath)
            print("{}. {}".format(x, SpeakerName.text))

unittest.main()