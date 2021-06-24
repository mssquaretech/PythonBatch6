from selenium import webdriver
import unittest
import time

class Yatra(unittest.TestCase):
    def setUp(self):
        global driver
        opt = webdriver.ChromeOptions()
        opt.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=opt)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.implicitly_wait(20)

    def test_YatraRoundtrip(self):
        roundTripXpath ="//a[@title = 'Round Trip']"
        roundTripEle = driver.find_element_by_xpath(roundTripXpath)
        roundTripEle.click()

        # Origin City Delhi select

        departureCityEle = driver.find_element_by_id("BE_flight_origin_city")
        departureCityEle.click()
        time.sleep(1)
        departureCityEle.send_keys("Delhi")
        time.sleep(2)
        xpathDelhi = "//div[@class = 'viewport']//span"
        driver.find_element_by_xpath(xpathDelhi).click()

        # Destination City Mumbai select

        arrivalEle = driver.find_element_by_id("BE_flight_arrival_city")
        arrivalEle.click()
        time.sleep(1)
        arrivalEle.send_keys("Mumbai")
        time.sleep(2)
        xpathMumbai = "//span/strong[text() = 'Mumbai']"
        driver.find_element_by_xpath(xpathMumbai).click()

        # departure date select

        driver.find_element_by_id("BE_flight_origin_date").click()
        time.sleep(1)
        depdate24Xpath = "//td[@id = '24/06/2021']"
        driver.find_element_by_xpath(depdate24Xpath).click()

        # arrival date select

        driver.find_element_by_id("BE_flight_arrival_date").click()
        time.sleep(1)
        arrivaldate26XPath = "//td[@id = '26/06/2021']"
        driver.find_element_by_xpath(arrivaldate26XPath).click()

        time.sleep(1)

        # updated code for add handle
        addXpath = "//button[contains(text(),'I Agree')]"
        addElement = driver.find_element_by_xpath(addXpath)

        if addElement.is_displayed():
            addElement.click()

        frameEle = driver.find_element_by_id("webklipper-publisher-widget-container-notification-frame")
        if frameEle.is_displayed():
            driver.switch_to.frame(frameEle)
            noteOfAdviceEle = driver.find_element_by_xpath("//b[contains(text(),'A note of advice')]")
            if noteOfAdviceEle.is_displayed():
                forwardEle = driver.find_element_by_xpath("//i[@class = 'we_forward']")
                forwardEle.click()

        driver.switch_to.default_content()

        # Click on Traveller
        travellerXpath = "//span[text() = 'Traveller']"
        driver.find_element_by_xpath(travellerXpath).click()

        # Click on plus to get 2 traveller
        plusXpath = "//span[@class = 'ddSpinnerPlus']"
        driver.find_element_by_xpath(plusXpath).click()

        # Prateek : To Contract the Traveller option - As there is a frame of a not of advice covering non stop flights checkbox
        # driver.find_element_by_xpath(travellerXpath).click()

        # Click on non stop flight
        checkBoxXpath = "//a[@title= 'Non Stop Flights']/i"
        time.sleep(1)
        driver.find_element_by_xpath(checkBoxXpath).click()

        # Click on Serach button to get the flight list
        driver.find_element_by_id("BE_flight_flsearch_btn").click()

        # def tearDown(self):
        #     driver.close()


unittest.main()