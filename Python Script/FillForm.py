from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class Formfill(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_fillForm(self):

        listofData = [('Narendra','Shakya','Australia','Approved'),('Karan','Negi','USA','Approved'),('Vikram','Pratap','Canada','Approved')]

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[@class='ws-btn w3-padding w3-round']")).perform()

        for i in listofData:

            driver.refresh()
            driver.find_element_by_id("fname").send_keys(i[0])
            driver.find_element_by_id("lname").send_keys(i[1])

            locateselect = driver.find_element_by_xpath("//select[@class='test']")
            locationSelect = Select(locateselect)

            if (i[2] == 'Australia'):
                locationSelect.select_by_visible_text("Australia")
            elif (i[2] == "Canada"):
                locationSelect.select_by_visible_text("Canada")
            elif (i[2] == "USA"):
                locationSelect.select_by_visible_text("USA")

            driver.find_element_by_xpath("//textarea[@class='test']").send_keys(i[3])
            driver.find_element_by_xpath("//a[@class='ws-btn w3-padding w3-round']").click()
            screen = driver.window_handles
            driver.switch_to.window(screen[0])


if __name__ == "__main__":
    unittest.main()


