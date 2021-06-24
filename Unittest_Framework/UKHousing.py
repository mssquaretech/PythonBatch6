from selenium import  webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class UKHousing(unittest.TestCase):

    def setUp(self):
        global driver
        # caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = 'none'
        # driver = webdriver.Chrome(desired_capabilities=caps)
        driver = webdriver.Chrome()
        driver.get("https://househunt.london.ac.uk/")
        driver.maximize_window()
        driver.implicitly_wait(20)

    def test_UK(self):
        findPropertyXpath = "//li[@class = 'nav-item']/child::a[text() = 'Find Your Property']"
        driver.find_element_by_xpath(findPropertyXpath).click()

        window = driver.window_handles
        driver.switch_to.window(window[1])

        searchXpath = "//div[@id= 'block-menu_block-2']/descendant::a[text() = 'Search']"
        searchEle = driver.find_element_by_xpath(searchXpath)

        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, searchXpath)))
        searchEle.click()

        uniXpath = "//div[@class = 'below']/descendant::div[text() = ' University ']"
        driver.find_element_by_xpath(uniXpath).click()

        uniListXpath = "//div[@class = 'options']/descendant::li/span"
        uniListEle = driver.find_elements_by_xpath(uniListXpath)

        for bucket in uniListEle:
            if bucket.text == 'Royal Academy of Music (RAM)':
                bucket.click()
                break

        campusXpath = "//div[text() = ' Campus ']"
        driver.find_element_by_xpath(campusXpath).click()

        campusListXpath = "//div[@class = 'options']/descendant::li/span"
        driver.find_element_by_xpath(campusListXpath).click()

        seeResultXpath = "//button[text() = 'See Results']"
        driver.find_element_by_xpath(seeResultXpath).click()

        buttonLoadXpath = "//button[@class = 'btn btn-lg btn-primary--hover']"
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, buttonLoadXpath)))

        dropDownXpath  = "//span[text() = 'Default']"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, dropDownXpath)))
        driver.find_element_by_xpath(dropDownXpath).click()

        lowToHighXpath = "//div[@class = 'options']/descendant::li/span[contains(text(), 'Low to High')]"
        driver.find_element_by_xpath(lowToHighXpath).click()

        buttonLoadXpath = "//button[@class = 'btn btn-lg btn-primary--hover']"
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, buttonLoadXpath)))

        flatListXpath = "//div[@class = 'row']/descendant::h3[@class = 'card-info__address mt-2 mb-2']"
        flatListElement = driver.find_elements_by_xpath(flatListXpath)

        count = len(flatListElement)

        # for i in range(1,6):
        #     print(flatListElement[i].text)

        for x in range (1,count):
            print(flatListElement[x].text)
            c = x+1
            if c == 6:
                break

    # def tearDown(self):
    #     driver.close()

unittest.main()