from selenium import webdriver
import time
import unittest

class YatraBookingTest(unittest.TestCase):

    def setUp(self):
        global Yatra
        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")
        Yatra = webdriver.Chrome(options=opt)
        Yatra.get("https://www.yatra.com/")
        Yatra.maximize_window()

    def test_YatraBooking(self):
        RoundTripXpath = "//a[@title='Round Trip']"
        RoundTripElement = Yatra.find_element_by_xpath(RoundTripXpath)
        RoundTripElement.click()
        time.sleep(1)

        OriginSearchBoxXpath = "//input[@name='flight_origin']"
        OriginSearchBoxElement = Yatra.find_element_by_xpath(OriginSearchBoxXpath)
        time.sleep(1)
        OriginSearchBoxElement.click()
        time.sleep(1)
        OriginSearchBoxElement.send_keys("Delhi")
        time.sleep(1)
        Yatra.find_element_by_xpath("//div[@class='ac_airport']").click()

        DestinationSearhBoxXpath = "//input[@name='flight_destination']"
        DestinationSearchBoxElement = Yatra.find_element_by_xpath(DestinationSearhBoxXpath)
        time.sleep(1)
        DestinationSearchBoxElement.click()
        time.sleep(1)
        DestinationSearchBoxElement.send_keys("Pune")
        time.sleep(1)
        Yatra.find_element_by_xpath("//div[@class='ac_airport']").click()

        DepartureBoxXpath = "//input[@name='flight_origin_date']"
        DepartureBoxElement = Yatra.find_element_by_xpath(DepartureBoxXpath)
        DepartureBoxElement.click()
        time.sleep(2)
        DepartureDateXpath = "//td[@data-date='10/06/2021']"
        DepartureDateElement = Yatra.find_element_by_xpath(DepartureDateXpath)
        DepartureDateElement.click()

        ReturnBoxXpath = "//input[@name='flight_destination_date']"
        ReturnBoxElement = Yatra.find_element_by_xpath(ReturnBoxXpath)
        ReturnBoxElement.click()
        time.sleep(2)
        ReturnDateXpath = "//td[@data-date='15/06/2021']"
        ReturnDateElement = Yatra.find_element_by_xpath(ReturnDateXpath)
        ReturnDateElement.click()

        TravellerXpath = "//span[contains(@class, 'travellerPaxBox')]"
        TravellerElement = Yatra.find_element_by_xpath(TravellerXpath)
        TravellerElement.click()
        time.sleep(2)
        AdultCountXpath = "//span[@class='ddSpinnerPlus']"
        AdultCountElement = Yatra.find_element_by_xpath(AdultCountXpath)
        AdultCountElement.click()

        Visible = Yatra.find_element_by_xpath("//iframe[contains(@title,'notification')]")
        if Visible.is_displayed():
            Yatra.switch_to.frame(Yatra.find_element_by_xpath("//iframe[contains(@title,'notification')]"))
            Yatra.find_element_by_xpath("//i[@class='we_close']").click()
            Yatra.switch_to.default_content()
        else:
            pass

        CheckBoxXpath = "//a[@title='Non Stop Flights']/i"
        CheckBoxElement = Yatra.find_element_by_xpath(CheckBoxXpath)
        CheckBoxElement.click()

        SearchFlightXpath = "//input[@value='Search Flights']"
        SearchFlightElement = Yatra.find_element_by_xpath(SearchFlightXpath)
        SearchFlightElement.click()

unittest.main()