from selenium import webdriver
import unittest

class MagicBricksWindow(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.magicbricks.com/flats-in-kolkata-for-sale-pppfs?mbtracker=google_paid_brand_desk_kolkata&ccode=brand_sem&gclid=CjwKCAjw-qeFBhAsEiwA2G7Nl3Si92__5tiPExHUuyE35pBB5fBav48Ci1_zRj9Cpa-gxHdst_CpJhoC0AAQAvD_BwE")
        driver.maximize_window()

    def test_MagicWindowCheck(self):
        searchXpath = "//div[contains(@id, 'resultBlockWrapper')]"
        searchelememtlist = driver.find_elements_by_xpath(searchXpath)

        # searchOneelement = driver.find_element_by_xpath(searchXpath)
        # searchOneelement.click()

        for proj in searchelememtlist:
            proj.click()

        Allwindowlist = driver.window_handles
        driver.switch_to.window(Allwindowlist[3])

        # projDetailsXpath = "//a[text() = 'Project Details']"
        # driver.find_element_by_xpath(projDetailsXpath).click()



unittest.main()
