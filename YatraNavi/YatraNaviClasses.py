import time
from selenium.webdriver import ActionChains
import unittest
from selenium import webdriver

class YatraNavClasses(unittest.TestCase):
    def setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        time.sleep(5)

    def test_SelectingValue(self):
        # global driver
        framepathelement = driver.find_element_by_xpath("//iframe[contains (@title,'notification-frame')]")
        driver.switch_to_frame(framepathelement)

        frameclose = "//i[contains (@class,'we_close')]"
        framecloseelement =driver.find_element_by_xpath(frameclose)

        action = ActionChains(driver)
        action.click(framecloseelement).perform()

        driver.switch_to_default_content()

        time.sleep(3)
        txtXpath = "//a[@title='Round Trip']"
        txtElement = driver.find_element_by_xpath(txtXpath)
        txtElement.click()

        depXpath = "//input[@id='BE_flight_origin_date']"
        depElement = driver.find_element_by_xpath(depXpath)
        depElement.click()

        time.sleep(2)

        selectDateXpath = "//table[@class='days-head day-container-table']/descendant::td[@class='depart-daybox']"
        selectElement = driver.find_element_by_xpath(selectDateXpath)
        selectElement.click()

        returnXpath = "//input[@id='BE_flight_arrival_date']"
        returnElement = driver.find_element_by_xpath(returnXpath)
        returnElement.click()

        time.sleep(2)
        selretuDateXpath = "//td[@data-date='26/05/2021']"
        selretuElement = driver.find_element_by_xpath(selretuDateXpath)
        selretuElement.click()

        traXpath = "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']/child::span[@class='totalCount']"
        traElement = driver.find_element_by_xpath(traXpath)
        time.sleep(2)
        traElement.click()

        traAddXpath = "//span[@class='ddSpinnerPlus'][1]"
        trzElement = driver.find_element_by_xpath(traAddXpath)
        trzElement.click()

        time.sleep(2)

        checkXpath = "//a[@for='BE_flight_non_stop']/i"
        checkElement = driver.find_element_by_xpath(checkXpath)
        checkElement.click()

        time.sleep(2)

        serchXpath = "//input[@value='Search Flights']"
        serchElement = driver.find_element_by_xpath(serchXpath)
        serchElement.click()

    # def tearDown(self):
    #     driver.close()

unittest.main()
# //span[contains(text(),'Departure Date')]
# //table[@class='days-head day-container-table']/descendant::td[@class='depart-daybox']
#//div[@class='day-container']/descendant::td[@data-date='24/05/2021']
#//td[@data-date='24/05/2021']