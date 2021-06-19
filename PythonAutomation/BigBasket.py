from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains

class BigBasketTest(unittest.TestCase):

    def setUp(self):
        global BBasket
        BBasket = webdriver.Chrome()
        BBasket.get("https://www.bigbasket.com/ps/?q=vegetables")
        BBasket.maximize_window()

    def test_BigBasketSelect(self):
        # Sorting the price via select function
        SortBox = "//select[@id='sel1']"
        SortBoxElement = BBasket.find_element_by_xpath(SortBox)

        DropDown = Select(SortBoxElement)
        DropDown.select_by_value("string:pricelth")
        time.sleep(4)

        # Scroll till Ginger last element

        GingerLastElementXpath = "//a[contains(text(),'Ginger')]/ancestor::div[@ng-if='!vm.selectedProduct.is_promo']/descendant::input[@ng-model='vm.startQuantity']"
        GingerLastElement = BBasket.find_element_by_xpath(GingerLastElementXpath)
        ScrollElement = ActionChains(BBasket)
        ScrollElement.move_to_element(GingerLastElement).perform()

        # To change the Ginger's weight from 100 to 250g

        Buttonbox = "//a[contains(text(),'Ginger')]/ancestor::div[@ng-if='!vm.selectedProduct.is_promo']/descendant::i[contains(@class,'caret')]"
        ButtonElement = BBasket.find_element_by_xpath(Buttonbox)
        ButtonElement.click()
        time.sleep(1)

        Price = "//a[contains(text(),'Ginger')]/ancestor::div[@ng-if='!vm.selectedProduct.is_promo']/descendant::li[@class='ng-scope']/descendant::span[@class='ng-binding' and text()='250 g']"
        PriceElement = BBasket.find_element_by_xpath(Price)
        PriceElement.click()
        time.sleep(1)

        AddtoCart = "//a[contains(text(),'Ginger')]/ancestor::div[@ng-if='!vm.selectedProduct.is_promo']/descendant::button[text()='Add ']"
        AddtoCartElement = BBasket.find_element_by_xpath(AddtoCart)
        AddtoCartElement.click()


unittest.main()