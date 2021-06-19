from selenium import webdriver
import unittest
import time

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class test_Househunt(unittest.TestCase):
    def setUp(self):
        global driver
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome(desired_capabilities=caps)

        #driver = webdriver.Chrome()
        driver.get("https://househunt.london.ac.uk/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_searchpage(self):

        findurpropertyXpath = "//li/a[contains(text(),'Find Your Property')]"
        findurpropertyXpathelement = driver.find_element_by_xpath(findurpropertyXpath)
        findurpropertyXpathelement.click()

        Allwindowlist = driver.window_handles
        driver.switch_to.window(Allwindowlist[1])

        searchXpath = "(//ul[@class='menu']/li/a[contains(text(),'Search')])[2]"
        searchXpathelement = driver.find_element_by_xpath(searchXpath)
        searchXpathelement.click()

        univerXpath = "//div[@class= 'placeholder ng-star-inserted' and contains(text(),' University ')]"
        univerXpathelement = driver.find_element_by_xpath(univerXpath)
        univerXpathelement.click()

        univerinputXpath = "//div[@class='filter ng-star-inserted']/input"
        univerinputXpathelement = driver.find_element_by_xpath(univerinputXpath)
        univerinputXpathelement.send_keys("Royal Academy")

        time.sleep(2)
        UniversityoptionXpath = "//span[contains(text(),'Royal Academy of Music (RAM)')]"
        UniversityoptionXpathelement = driver.find_element_by_xpath(UniversityoptionXpath)
        UniversityoptionXpathelement.click()

        campusXpath = "//div[@class='placeholder ng-star-inserted' and contains(text(),'Campus')]"
        campusXpathelement =driver.find_element_by_xpath(campusXpath)
        campusXpathelement.click()
        campusresXpath = "//span[@class='ng-star-inserted' and contains(text(),'Campus')]"
        campusresXpathelement = driver.find_element_by_xpath(campusresXpath)
        campusresXpathelement.click()

        seeresultXpath = "//button[contains(text(),'See Results')]"
        seeresultXpathelement = driver.find_element_by_xpath(seeresultXpath)
        seeresultXpathelement.click()

        listXpath = "(//button[contains(text(),'List')])[2]"
        WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, listXpath)))

        listviewXpath = "(//div[@class='value ng-star-inserted'])[3]"
        listviewXpathelement = driver.find_element_by_xpath(listviewXpath)
        listviewXpathelement.click()

        listoptionXpath = "//span[contains(text(),'Price: Low to High')]"
        listoptionXpathelemrnt = driver.find_element_by_xpath(listoptionXpath)
        listoptionXpathelemrnt.click()
        time.sleep(5)

        waitelemXpath =  "//button[@class='btn btn-lg btn-primary--hover']"

        WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.XPATH, waitelemXpath)))
        time.sleep(10)
        #(EC.element_to_be_clickable((By.XPATH, seeresultXpath)))

        sresultXpath = "//div/div/div/h3[contains(@class,'card-info')]"
        sresultXpathElement = driver.find_elements_by_xpath(sresultXpath)
        count = len(sresultXpathElement)

        for i in range(count):
            if i <= 5:
                print(sresultXpathElement[i].text)
            else:
                pass


unittest.main()