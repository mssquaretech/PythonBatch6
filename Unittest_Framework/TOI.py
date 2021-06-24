from selenium import webdriver
import unittest
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TOI(unittest.TestCase):

    def setUp(self):
        global driver
        caps = DesiredCapabilities.CHROME
        caps["pageLoadStrategy"] = "none"
        driver = webdriver.Chrome(desired_capabilities=caps)
        driver.get("https://timesofindia.indiatimes.com")
        driver.maximize_window()
        driver.implicitly_wait(20)

    def test_TOI(self):

        # Pop up handle:
        waitXpath = "//p[text() = 'Get instant notifications as they happen']"
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, waitXpath)))

        popUPxpath = "//a[text() = 'Not Now']"
        driver.find_element_by_xpath(popUPxpath).click()

        # check for BLOG to scroll to that:
        blogXpath = "//a[@data-newga = 'Section_Actions#HeadingClick-Blogs']"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, blogXpath)))
        scrollElement =  driver.find_element_by_xpath("//a[@data-newga = 'Section_Actions#HeadingClick-Blogs']")
        action = ActionChains(driver)
        action.move_to_element(scrollElement).perform()

        # check for Visibility of Poll:
        pollVisiXPATH = "//div[text() = 'Poll']"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, pollVisiXPATH)))

        # Cast vote:
        pollXpath = "//div[@class = '_26fds']/label/input"
        PollElement = driver.find_element_by_xpath(pollXpath)
        PollElement.click()

        buttonElement = driver.find_element_by_xpath("//button[text() = 'SUBMIT']")
        buttonElement.click()

        # check for successful vote cast:
        voteCastCheckXpath = "//h4[text() = 'Congratulations!']"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, voteCastCheckXpath)))

        # scroll to Cartoon to get Navbharat times:
        cartoonElement = driver.find_element_by_xpath("//a[@data-newga = 'cartoonsSection_Actions#HeadingClick']")
        action = ActionChains(driver)
        action.move_to_element(cartoonElement).perform()

        # check for Navbharat times:
        navBharatXpath = "//a[@data-newga = 'NBT-Actions#NBT_Click']"
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, navBharatXpath)))

        # Switch to Navbharat frame:
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@title, 'Navbharat')]"))

        listXpath = "//span[@id ='dotsblk']/ul/li"
        # listElement = driver.find_elements_by_xpath(listXpath)

        # for list in listElement:
        #     list.click()

        listElement = driver.find_elements_by_xpath("//span[@id='dotsblk']/descendant::li")
        for i in range(1, len(listElement)):
            driver.find_element_by_xpath("//span[@id='dotsblk']/descendant::li[" + str(i) + "]").click()
            currentlink = "//span[@id='dotsblk']/descendant::a[" + str(i) + "]/parent::li[@class='current']"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, currentlink)))

unittest.main()



