import time
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities

class ukHousing(unittest.TestCase):
    def setUp(self):
        global driver

        caps = DesiredCapabilities.CHROME
        caps["pageLoadStrategy"]="normal"
        driver = webdriver.Chrome(desired_capabilities=caps)
        driver.get("https://househunt.london.ac.uk/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_uk(self):
        print(driver.title)
        driver.find_element_by_xpath("//ul[@class='ng-star-inserted']/child::li/a[contains(text(),'Find Your Property')]").click()

        NextwindowHandle = driver.window_handles
        driver.switch_to.window(NextwindowHandle[1])

        driver.find_element_by_xpath("(//ul[@class='menu']/li/a[contains(text(),'Search')])[2]").click()

        driver.find_element_by_xpath("//div[@style='z-index: 10;']").click()

        driver.find_element_by_xpath("//span[contains(text(),'RAM')]").click()

        driver.find_element_by_xpath("//div[@style='z-index: 9;']").click()

        driver.find_element_by_xpath("//span[contains(text(),'Main')]").click()

        driver.find_element_by_xpath("//button[contains(text(),'See')]").click()

        time.sleep(30)

        driver.find_element_by_xpath("(//div[@class='toggle ng-star-inserted'])[4]").click()

        driver.find_element_by_xpath("//div[@class='col-md-12 d p-0 group-view d-none d-md-flex']/descendant::span[contains(text(),'Price')]").click()

        wait = "//button[@class='btn btn-lg btn-primary--hover loading']"
        WebDriverWait(driver, 50).until(EC.invisibility_of_element_located((By.XPATH, wait)))

        printProperty = "(//h3[@class='card-info__address mt-2 mb-2'])"
        printPropertyElement = driver.find_elements_by_xpath(printProperty)
        rangeOf = len(printPropertyElement)

        for bucket in range(1,rangeOf):
            if bucket <= 5:
                print(printPropertyElement[bucket].text)
            else:
                break

    # def tearDown(self):
    #     time.sleep(10)
    #     driver.close()

unittest.main()