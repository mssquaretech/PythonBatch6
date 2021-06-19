from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import time


class FillUserForm(unittest.TestCase):

    def setUp(self):
        global W3School
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        W3School = webdriver.Chrome(desired_capabilities=caps)
        W3School.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
        W3School.maximize_window()

    def test_FormFillng(self):

        VisibleTextXpath = "//label[text()='First Name']"
        WebDriverWait(W3School, 10).until(EC.visibility_of_element_located((By.XPATH, VisibleTextXpath)))

        Details = [("Narendra", "Shakya", "Australia", "Approved"),
                   ("Vikram", "Pratap", "Canada", "Approved"),
                   ("Karan", "Negi", "USA", "Approved")]

        Listcount = len(Details)

        for x in Details:

            firstnameElement = W3School.find_element_by_id("fname")
            firstnameElement.send_keys(x[0])
            lastnameElement = W3School.find_element_by_id("lname")
            lastnameElement.send_keys(x[1])

            # Value1 = "Australia"
            # if x[2] == Value1:
            #     currentvalue =

            CountryDropDownElement = W3School.find_element_by_id("country")
            SelectDropDown = Select(CountryDropDownElement)
            SelectDropDown.select_by_visible_text(x[2])

            TextBodyXpath = "//textarea[@class='test']"
            TextBodyXpathElement = W3School.find_element_by_xpath(TextBodyXpath)
            TextBodyXpathElement.send_keys(x[3])

            W3School.find_element_by_xpath("//a[text()='Submit']").click()

            ListofWindows = W3School.window_handles
            W3School.switch_to.window(ListofWindows[0])

            time.sleep(2)
            Listcount -= 1

            if Listcount >= 1:
                W3School.find_element_by_id("fname").clear()
                W3School.find_element_by_id("lname").clear()
                W3School.find_element_by_xpath("//textarea[@class='test']").clear()
            else:
                pass

if __name__ == "__main__":
    unittest.main()