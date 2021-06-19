from selenium import webdriver
import unittest

class ListandTuple(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
        driver.maximize_window()

    def test_entries(self):

        entryTuple = [('Iron', 'Man', 'Australia', 'Master'), ('wonder', 'women', 'Canada', 'Master'), ('Thunder', 'Thor', 'USA', 'Master')]


        for entries in entryTuple:
            # submXpath = "//a[text()='Submit']"
            # submXpathElement = driver.find_element_by_xpath(submXpath)

            driver.find_element_by_id('fname').send_keys(entries[0])
            driver.find_element_by_id('lname').send_keys(entries[1])
            driver.find_element_by_id('country').send_keys(entries[2])
            driver.find_element_by_xpath("//textarea[@class='test']").send_keys(entries[3])
            driver.find_element_by_xpath("//a[text()='Submit']").click()

            Allwindowlist = driver.window_handles
            driver.switch_to.window(Allwindowlist[0])

            driver.find_element_by_id('fname').clear()
            driver.find_element_by_id('lname').clear()
            driver.find_element_by_xpath("//textarea[@class='test']").clear()




            # if entries == entryTuple[0]:
            #     driver.find_element_by_xpath("//a[text()='Submit']").click()

            # else:
            #     Newwindowlist = driver.window_handles
            #     driver.switch_to.window(Newwindowlist[3])






            #driver.switch_to.window(submXpathElement).find_element_by_class_name("test").send_keys(entries[3])


        # submXpath = "//a[text()='Submit']"
        # submXpathElement = driver.find_element_by_xpath(submXpath)
        # submXpathElement.click()

unittest.main()

