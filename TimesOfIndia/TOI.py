import time

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
# from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class TOI(unittest.TestCase):

    def setUp(self):
        global driver
        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")
        # driver = webdriver.Chrome()
        # caps = DesiredCapabilities().CHROME
        # caps["loadPageStrategy"] = "none"
        driver = webdriver.Chrome(options=opt)

        driver.get("https://timesofindia.indiatimes.com")
        driver.maximize_window()
        driver.implicitly_wait(10)


    def test_toiPoll(self):

        # driver.find_element_by_xpath("//a[@href='javascript://']").click()

        pollXpath = "//button[@class='InRm5  ']"
        pollElement = driver.find_element_by_xpath(pollXpath)

        action = ActionChains(driver)
        action.move_to_element(pollElement).perform()

        buttonElement = driver.find_element_by_xpath("//div[@class='_26fds']//label[(last())]/input")
        buttonValue = buttonElement.get_attribute("value")
        if(buttonValue=='No'):
            buttonElement.click()
        elif(buttonValue=='Disagree'):
            buttonElement.click()

        driver.find_element_by_xpath("//button[@class='InRm5  dY9DU']").click()

        messageXpath = "//div[@class='_2K_up']"
        messageElement = driver.find_element_by_xpath(messageXpath)
        print(messageElement.text)

        frameElement = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//iframe[@title='Prime Blocker']")))

        driver.switch_to.frame(frameElement)

        toiNotification = "//span[@data-prime='close-ad-free-nudge']"
        toiNotificationElement = driver.find_element_by_xpath(toiNotification)
        toiNotificationElement.click()

        driver.switch_to.default_content()

        navBhaElement = driver.find_element_by_xpath("//a[starts-with(text(),'cartoons')]")

        action = ActionChains(driver)
        action.move_to_element(navBhaElement).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@title='Navbharat Times']"))

        navBhaScroll = "//span[@id='dotsblk']/descendant::li"
        navBha= driver.find_elements_by_xpath(navBhaScroll)
        rangeofLenghth = len(navBha)
        # print(rangeofLenghth)

        for i in range(1,rangeofLenghth):
            driver.find_element_by_xpath("//span[@id='dotsblk']/descendant::li["+str(i)+"]").click()
            currentlink = "//span[@id='dotsblk']/descendant::a[" + str(i) + "]/parent::li[@class='current']"
            print(driver.find_element_by_xpath("//div[@id='homePicGallery']/descendant::a[" + str(i) + "]/span").text)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,currentlink)))

    # def tearDown(self):
    #     driver.quit()
unittest.main()