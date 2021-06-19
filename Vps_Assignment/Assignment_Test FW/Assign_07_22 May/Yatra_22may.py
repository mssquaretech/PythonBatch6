from selenium import webdriver

import time
import unittest

class testingYatra(unittest.TestCase):
    def test_Scrollcheck(self):

        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com")
        driver.maximize_window()

        #Round Trip
        tripXpath = "//a[@title='Round Trip']"
        tripXpath = driver.find_element_by_xpath(tripXpath)
        tripXpath.click()

        #from Delhi
        departXpath = "//input[@name='flight_origin' and @id='BE_flight_origin_city']"
        departXpath = driver.find_element_by_xpath(departXpath)
        departXpath.send_keys("New Delhi")
        time.sleep(2)

        departResultXpath = "//p[@class='ac_cityname']/span[text()='(DEL)']"
        departResultXpath = driver.find_element_by_xpath(departResultXpath)
        departResultXpath.click()
        time.sleep(2)

        goingtXpath = "//input[@name='flight_destination' and @id='BE_flight_arrival_city']"
        goingtXpath = driver.find_element_by_xpath(goingtXpath)
        goingtXpath.send_keys("Mumbai")
        time.sleep(2)

        #to Mumbai
        goingResultXpath = "//strong[text()='Mumbai']"
        goingResultXpath = driver.find_element_by_xpath(goingResultXpath)
        goingResultXpath.click()
        time.sleep(2)

        #Dep Date: 24th May
        DepartdateXpath = "//input[@name='flight_origin_date' and @id='BE_flight_origin_date']"
        DepartdateXpath = driver.find_element_by_xpath(DepartdateXpath)
        DepartdateXpath.click()
        time.sleep(2)

        DepartdateXpathresult = "//td[@data-date='24/05/2021']"
        DepartdateXpathresult = driver.find_element_by_xpath(DepartdateXpathresult)
        DepartdateXpathresult.click()
        time.sleep(2)

        #Return Date: 26th May
        ReturndateXpath = "//input[@name='flight_destination_date']"
        ReturndateXpath = driver.find_element_by_xpath(ReturndateXpath)
        ReturndateXpath.click()
        time.sleep(2)

        ReturndateXpathresult = "//td[@data-date='26/05/2021']"
        ReturndateXpathresult = driver.find_element_by_xpath(ReturndateXpathresult)
        ReturndateXpathresult.click()
        time.sleep(2)

        flightstopXpath = "//div[@class='filter-list']/a[@title='Non Stop Flights']/i"
        flightstopXpath = driver.find_element_by_xpath(flightstopXpath)
        flightstopXpath.click()

        # Economy
        #economyXpath = "//li[@class='enabled _msddli_ selected']/span[text()='Economy']"
        #economyXpath = driver.find_element_by_xpath(economyXpath)
        #economyXpath.click()

        #2 Adults
        travellerXpath = "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']"
        travellerXpath = driver.find_element_by_xpath(travellerXpath)
        travellerXpath.click()
        time.sleep(2)

        travellercountXpath = "//div[@data-flightagegroup='adult' and @class='pax-limit clearfix col-x-fluid']/div/div/span[@class='ddSpinnerPlus']"
        travellercountXpath = driver.find_element_by_xpath(travellercountXpath)
        travellercountXpath.click()
        time.sleep(2)


        searchflightXpath = "//input[@value='Search Flights']"
        searchflightXpath = driver.find_element_by_xpath(searchflightXpath)
        searchflightXpath.click()
        time.sleep(10)








unittest.main()