from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains

class Yatrabooking(unittest.TestCase):

    def setUp(self) :

        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

    def test_booking(self):

        time.sleep(5)

        framepathelement = driver.find_element_by_xpath("//iframe[contains (@title,'notification-frame')]")
        driver.switch_to.frame(framepathelement)

        frameclose = "//i[contains (@class,'we_close')]"
        framecloseelement =driver.find_element_by_xpath(frameclose)
        action = ActionChains(driver)
        action.click(framecloseelement).perform()

        driver.switch_to.default_content()

        time.sleep(3)
        RoundTrip = "//a[@data-flighttrip='R']"
        RoundTripElement = driver.find_element_by_xpath(RoundTrip)
        RoundTripElement.click()

        Origin = "//input[@id='BE_flight_origin_city']"
        OriginElement = driver.find_element_by_xpath(Origin)
        OriginElement.click()
        OriginElement.send_keys("Del")

        time.sleep(3)
        DepartAir = "//div[@class ='ac_airport']//p[contains (text(),'New Delhi')]"
        DepartAirElement = driver.find_element_by_xpath(DepartAir)
        DepartAirElement.click()

        time.sleep(3)
        arrival = "//input[@id='BE_flight_arrival_city']"
        arrivalelement = driver.find_element_by_xpath(arrival)
        arrivalelement.click()
        arrivalelement.send_keys("Mum")

        time.sleep(3)
        arrivalcity = "//span[contains(text(),'BOM')]/ancestor::p"
        arrivalcityelement = driver.find_element_by_xpath(arrivalcity)
        arrivalcityelement.click()

        origiondate = "//input[@id='BE_flight_origin_date']"
        origiondateelement = driver.find_element_by_xpath(origiondate)
        origiondateelement.click()

        time.sleep(2)
        depaturedate = "//td[@data-date='24/05/2021']"
        depaturedateelement = driver.find_element_by_xpath(depaturedate)
        depaturedateelement.click()

        time.sleep(3)
        returndate = "//td[@data-date='26/05/2021']"
        returndateelement = driver.find_element_by_xpath(returndate)
        returndateelement.click()

        time.sleep(3)
        traveller = "//label[@class='travellerLabel']"
        travellerelement = driver.find_element_by_xpath(traveller)
        travellerelement.click()

        addadult = "//span[@class='ddSpinnerPlus']"
        addadultelement = driver.find_element_by_xpath(addadult)
        addadultelement.click()

        time.sleep(2)

        nonstop = "//a[@for='BE_flight_non_stop']/input[@id ='BE_flight_non_stop']/preceding-sibling::i"
        nonstopelement = driver.find_element_by_xpath(nonstop)
        nonstopelement.click()

        search ="//input[@id='BE_flight_flsearch_btn']"
        searchelement=driver.find_element_by_xpath(search)
        searchelement.click()

unittest.main()
