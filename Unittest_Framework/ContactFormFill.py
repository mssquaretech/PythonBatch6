from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class ContactForm(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
        driver.maximize_window()
        driver.implicitly_wait(20)

    def test_Contactfill(self):

        tryITXpath = "//a[@class = 'ws-btn' and  contains(text() , 'Try it ')]"
        tryITele = driver.find_element_by_xpath(tryITXpath)
        action = ActionChains(driver)
        action.move_to_element(tryITele).perform()

        ListofTupple = [('Mona','Kar','USA','Approved'),('Karan', 'Negi', 'Canada', 'Approved'),('Garima', 'Singh', 'Australia', 'Approved')]

        for i in ListofTupple:
            driver.find_element_by_id("fname").send_keys(i[0])
            driver.find_element_by_id("lname").send_keys(i[1])
            dropdownEle = driver.find_element_by_id("country")
            Select(dropdownEle).select_by_visible_text(i[2])
            driver.find_element_by_xpath("//textarea[@placeholder = 'Write something..']").send_keys(i[3])
            driver.find_element_by_xpath("//a[text() = 'Submit']").click()

            windowList = driver.window_handles
            driver.switch_to.window(windowList[0])

            driver.find_element_by_id("fname").clear()
            driver.find_element_by_id("lname").clear()
            driver.find_element_by_xpath("//textarea[@placeholder = 'Write something..']").clear()

if __name__ == '__main__':
    unittest.main()



