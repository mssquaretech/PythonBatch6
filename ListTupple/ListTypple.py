import time

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains

class listTupple(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
        driver.maximize_window()

    def test_FillForm(self):
        # scrollbar = driver.find_element_by_xpath("//a[@class='ws-btn']")

        # action = ActionChains(driver)
        # action.move_to_element(scrollbar).perform()

        listofTuple = [('Mohit','Kankriya','USA','Superb'),('Rohit','Kumar','Australia','2nd Time'),('Rakesh','Uma','Canada','Finally')]

        for list in listofTuple:
            driver.find_element_by_id("fname").send_keys(list[0])
            driver.find_element_by_id("lname").send_keys(list[1])
            driver.find_element_by_id("country").send_keys(list[2])
            driver.find_element_by_xpath("//textarea[@placeholder='Write something..']").send_keys(list[3])
            driver.find_element_by_xpath("//a[text()='Submit']").click()

            AllWindowHandleList =driver.window_handles
            driver.switch_to.window(AllWindowHandleList[0])
            time.sleep(2)
            driver.refresh()

    def tearDown(self):
            driver.quit()

unittest.main()