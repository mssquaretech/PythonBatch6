from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class NestedFrame(unittest.TestCase):
    def setUp(self):
        global driver
        opt = webdriver.ChromeOptions()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=opt)
        driver.get("https://www.hotfrog.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_Nested(self):

        adXPATH = "//head/meta[@name = 'viewport']/following-sibling::title"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, adXPATH)))
        get_title = driver.title
        print("Webpage Title: ", get_title)

        scrollXpath = "//h2[text() = 'Recent Activity']"
        scrollEle = driver.find_element_by_xpath(scrollXpath)
        action = ActionChains(driver)
        action.move_to_element(scrollEle).perform()

        frameELE = driver.find_element_by_id("aswift_1")
        driver.switch_to.frame(frameELE)

        addTitleXpath = "//body[@class = 'jar']/descendant::a[@dir = 'auto']"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, addTitleXpath)))
        addTitleEle = driver.find_element_by_xpath(addTitleXpath)
        print("Title of Add is: ", addTitleEle.text)

        nestedXpath = "//body[@class = 'jar']/iframe"
        nestedEle = driver.find_element_by_xpath(nestedXpath)
        driver.switch_to.frame(nestedEle)

        nestedSRCXpath = "//script[@type = 'text/javascript']"
        nessrcEle = driver.find_element_by_xpath(nestedSRCXpath).get_attribute('src')
        driver.get(nessrcEle)

        srcElement = driver.find_element_by_xpath("//*")
        variable = srcElement.text
        this_count = variable.count("this")
        print("Total count of this is: ", this_count)

if __name__ == '__main__':
    unittest.main()