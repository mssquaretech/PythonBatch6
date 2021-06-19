from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TOI(unittest.TestCase):

    def setUp(self):

        global driver
        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=opt)
        driver.get("https://timesofindia.indiatimes.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_timesofIndia(self):

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//div[@class='_26fds']/label[last()]")).perform()

        buttonelement = driver.find_element_by_xpath("//div[@class='_26fds']/label[last()]/input")
        buttonvalue = buttonelement.get_attribute("value")
        if ( buttonvalue == 'No'):
            buttonelement.click()
        elif( buttonvalue == 'Disagree'):
            buttonelement.click()

        driver.find_element_by_xpath("//div[@class='_26fds']/button").click()

        WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,"//iframe[@title='Prime Blocker']")))
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Prime Blocker']"))
        driver.find_element_by_xpath("//span[@class='close_ad_free']").click()

        driver.switch_to.default_content()

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//a[text()='Infographics']")).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Navbharat Times']"))
        linkradiobutton = driver.find_elements_by_xpath("//div[@id='homePicGallery']/descendant::a")
        rangeoflink = len(linkradiobutton)

        listElement = driver.find_elements_by_xpath("//span[@id='dotsblk']/descendant::li")

        for i in range(1, len(listElement)):
            driver.find_element_by_xpath("//span[@id='dotsblk']/descendant::li[" + str(i) + "]").click()
            currentlink = "//span[@id='dotsblk']/descendant::a[" + str(i) + "]/parent::li[@class='current']"
            driver.find_element_by_xpath("//div[@id='homePicGallery']/descendant::a[" + str(i) + "]/span").click()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, currentlink)))


if __name__ == '__main__':
    unittest.main()

