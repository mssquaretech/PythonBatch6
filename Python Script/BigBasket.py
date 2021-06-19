import time

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Bigbasket(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.bigbasket.com/")
        driver.implicitly_wait(15)
        driver.maximize_window()

    def test_Vegilist(self):

        shopCatalogy = "//a[contains (@class,'meganav-shop')]"
        shopCatalogyElement = driver.find_element_by_xpath(shopCatalogy)
        action = ActionChains(driver)
        action.click_and_hold(shopCatalogyElement).perform()

        vegiPath = "(//div[contains(@class,'dont-show')]/descendant::a[text()='Vegetables'])[2]"
        vegiPathElement = driver.find_element_by_xpath(vegiPath)
        action.click(vegiPathElement).perform()

        priceFilterpath ="//Select[@id='sel1']"
        priceFilterpathElement = driver.find_element_by_xpath(priceFilterpath)

        choosefilter = Select(priceFilterpathElement)
        choosefilter.select_by_visible_text("Price - Low to High")

        valuetobevisible = "//option[@value='string:pricelth' and @selected='selected']"
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,valuetobevisible)))

        productName = "//div[@qa='product_name']/a[contains(text(),'Tomato - Local, Organically Grown')]/parent::div/following-sibling::div[contains(@class,'qnty-selection')]//button"
        productNameElement= driver.find_element_by_xpath(productName)
        prodscroll = ActionChains(driver)
        prodscroll.move_to_element(productNameElement).perform()

        productNameElement.click()

        selectvalue = "//div[@qa='product_name']/a[contains(text(),'Tomato - Local, Organically Grown')]/parent::div/following-sibling::div[contains(@class,'qnty-selection')]//button/..//span[text()='1 kg']"
        selectvalueElement = driver.find_element_by_xpath(selectvalue)
        selectvalueElement.click()

        addbasket = "//div[@qa='product_name']/a[contains(text(),'Tomato - Local, Organically Grown')]/parent::div/following-sibling::div[contains(@class,'add-bskt')]//button"
        addbasketElement = driver.find_element_by_xpath(addbasket)
        addbasketElement.click()

unittest.main()