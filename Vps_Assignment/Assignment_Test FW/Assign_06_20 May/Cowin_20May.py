from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest

class TestingCowin(unittest.TestCase):
    def test_ScrollCheck(self):

        driver = webdriver.Chrome()
        driver.get("https://www.cowin.gov.in/home")
        driver.maximize_window()

        time.sleep(3)

        searchXpath = "//input[@placeholder='Enter your PIN']"
        searchXpath = driver.find_element_by_xpath(searchXpath)
        searchXpath.send_keys("824101")

        searchPinXpath = "//button[@class='pin-search-btn']"
        searchPinXpath = driver.find_element_by_xpath(searchPinXpath)
        searchPinXpath.click()
        time.sleep(5)

        searchAgeXpath = "//label[text()=' Age 45+ ']"
        searchAgeXpath = driver.find_element_by_xpath(searchAgeXpath)
        searchAgeXpath.click()

        time.sleep(5)

        #searchSlotXpath = "(//div[@class='col-sm-12 col-md-12 col-lg-12'])[1]//a[@title='Fully Booked']"
        #searchSlotXpath = "(//div[@class='col-sm-12 col-md-12 col-lg-12'])[1]"
        #slotElement = driver.find_element_by_xpath(searchSlotXpath).get_attribute(searchSlotXpath)
        #print(slotElement)

        searchHospXpath = "//h5[@class='center-name-title']"
        hospElement = driver.find_element_by_tag_name('h5')
        #hospElement = driver.find_element_by_xpath('(//div[@class="col-sm-12 col-md-12 col-lg-12"])[1]').find_element_by_tag_name('h5')
        #find_element_by_xpath(searchHospXpath).get_attribute()

        time.sleep(2)

        print(hospElement.text)
        print()


        time.sleep(5)

        # action = ActionChains(driver)
        # action.move_to_element(searchSlotXpath).perform()
        # time.sleep(10)

unittest.main()



