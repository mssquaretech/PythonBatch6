from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import unittest

class TestingCowin(unittest.TestCase):
    def test_cowin(self):
        driver = webdriver.Chrome()
        driver.get("https://www.cowin.gov.in/home")
        driver.maximize_window()

        time.sleep(1)
        viewReportXpath = "//a[contains(text(),'View full report')]"
        viewReportElement = driver.find_element_by_xpath(viewReportXpath)

        action = ActionChains(driver)
        action.move_to_element(viewReportElement).perform()

        time.sleep(1)
        pinCodeElemet = driver.find_element_by_id("mat-input-0")
        pinCodeElemet.send_keys("700004")

        searchXpth = "//button[contains(text(),' Search')]"
        searchElement = driver.find_element_by_xpath(searchXpth)
        searchElement.click()

        age45Xpath = "//label[contains(text(), 'Age 45+')]"
        age45Element = driver.find_element_by_xpath(age45Xpath)
        age45Element.click()

        time.sleep(1)
        hospital1Xpath = "//h5[@class = 'center-name-title']"
        hospital1Elemnt = driver.find_element_by_xpath(hospital1Xpath)

        slot1Xpath = "(//ul[contains(@class, 'slot-available-wrap')]//a)[2]"
        slot1Element = driver.find_element_by_xpath(slot1Xpath)

        hospital2Xpath = "(//h5[@class = 'center-name-title'])[2]"
        hospital2Elemnt = driver.find_element_by_xpath(hospital2Xpath)

        slot2Xpath = "(//ul[contains(@class, 'slot-available-wrap')]//a)[3]"
        slot2Element = driver.find_element_by_xpath(slot2Xpath)

        print("1st Hospital name:", hospital1Elemnt.text, "-- Vaccine slot Status of 21st May :", slot1Element.text)
        print("2ndHospital name:", hospital2Elemnt.text, "-- Vaccine slot Status of 21st May :", slot2Element.text)

unittest.main()





