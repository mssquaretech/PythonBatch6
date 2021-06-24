from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BigBasket(unittest.TestCase):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.bigbasket.com/ps/?q=vegetables")
    driver.maximize_window()
    driver.implicitly_wait(10)

    def test_BigBasket(self):
        sortbyPriceElement = driver.find_element_by_id("sel1")
        Select(sortbyPriceElement).select_by_value("string:pricelth")

        time.sleep(3)

        dropdownXpath = "(//a[@uib-tooltip = 'Ginger - Organically Grown']/parent::div/following-sibling::div/descendant::button)[1]"
        time.sleep(3)
        dropdownElement = driver.find_element_by_xpath(dropdownXpath)
        time.sleep(2)
        dropdownElement.click()

        dd250gXpath = "(//a[@uib-tooltip = 'Ginger - Organically Grown']/parent::div/following-sibling::div/descendant::button)[1]/following-sibling::ul//span[text() = '250 g']"
        dd250gEle = driver.find_element_by_xpath(dd250gXpath)
        dd250gEle.click()

        buttonAddCartXpath = "(//a[@uib-tooltip = 'Ginger - Organically Grown']/parent::div/following-sibling::div/descendant::button)[2]"
        driver.find_element_by_xpath(buttonAddCartXpath).click()
        time.sleep(1)

        # to handle the grey screen
        driver.find_element_by_id("city-drop-overlay").click()

        # to check the basket:
        checkBasketcontent = driver.find_element_by_xpath("//span[@class = 'basket-content']")
        checkBasketcontent.click()

        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"  ")))

unittest.main()


