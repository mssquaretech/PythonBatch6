from selenium import webdriver

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Househunt(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("https://househunt.london.ac.uk/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_houseHunt(self):
        findoutProperty = "//nav[@class='primary-nav']/descendant::a[contains(@href,'find-your-property')]"
        driver.find_element_by_xpath(findoutProperty).click()

        countopenWindow = driver.window_handles
        driver.switch_to.window(countopenWindow[1])

        driver.find_element_by_xpath("//aside[@id='sidebar-first']/descendant::li[contains(@class,'first leaf')]").click()

        driver.find_element_by_xpath("//div[@class='container-fluid']//div[text()=' University ']").click()

        selectuniversityXpath = "//div[@class='options']"
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,selectuniversityXpath)))

        driver.find_element_by_xpath("//span[text()='Royal Academy of Music (RAM)']").click()

        driver.find_element_by_xpath("//div[text()=' Campus ']").click()
        selectoptionunderCampus = "//span[text()='Main Campus']"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,selectoptionunderCampus)))

        driver.find_element_by_xpath(selectoptionunderCampus).click()

        submitclick ="//div[@class='row filter-row']/descendant::div[@class='submit-group']/button"
        driver.find_element_by_xpath(submitclick).click()

        resultsshown = "//p[contains(@class,'number-of-result')]"
        WebDriverWait(driver,45).until(EC.visibility_of_element_located((By.XPATH,resultsshown)))
        driver.get_screenshot_as_file("SearchResult.png")

        filterresultXpath = "//div[contains(@class,'col-md-2 ng-touched')]/descendant::div[@class='value ng-star-inserted']"
        driver.find_element_by_xpath(filterresultXpath).click()

        filterselect = "//span[contains(text(),'Low to High')]"
        Checkforvalue = driver.find_element_by_xpath(filterselect)
        Checkforvalue.click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,filterselect)))

        WebDriverWait(driver,45).until(EC.invisibility_of_element_located((By.XPATH,"//button[@class='btn btn-lg btn-primary--hover loading']")))

        resultsnameXapth = "//h3[@class='card-info__address mt-2 mb-2']"
        resultname = driver.find_elements_by_xpath(resultsnameXapth)
        numberofresults = len(resultname)

        for i in range(1,numberofresults):
            if( i < 6 ):
                listofname = driver.find_element_by_xpath("(//h3[@class='card-info__address mt-2 mb-2'])[" + str(i) + "]").text
                print(listofname)
            else:
                break


if __name__ == '__main__':
    unittest.main()