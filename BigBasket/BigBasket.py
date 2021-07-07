from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class test_BigBasket(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.bigbasket.com/ps/?q=vegetables")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_Big(self):
        listXpath = "//select[@id='sel1']"
        listElement = driver.find_element_by_xpath(listXpath)
        # time.sleep(2)
        Select(listElement).select_by_value("string:pricelth")

        EConditionXpath = "//option[@value='string:pricelth' and @selected='selected']"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,EConditionXpath)))

        # time.sleep(2)

        scrollXpath = "//span[@class='bskt-icon']"
        scrollElement = driver.find_element_by_xpath(scrollXpath)

        # time.sleep(5)
        actions = ActionChains(driver)
        actions.move_to_element(scrollElement).perform()
        # time.sleep(2)

        gramXpath = "//span[@ng-if='!product.attrs.type']"
        gramElement = driver.find_element_by_xpath(gramXpath)
        gramElement.click()
        # time.sleep(2)

        selPriceXpath = "//a[@ng-click='vm.onProductChange(allProducts)']"
        selElement = driver.find_element_by_xpath(selPriceXpath)
        selElement.click()
        # time.sleep(2)

        clickButtonXpath = "//button[@ng-click='vm.addToBasket(vm.selectedProduct);']"
        clickButtonElement = driver.find_element_by_xpath(clickButtonXpath)
        clickButtonElement.click()
        # time.sleep(2)

    # def tearDown(self):
    #     # time.sleep(10)
    #     driver.quit()

unittest.main()