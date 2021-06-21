from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time

class NestedFrame(unittest.TestCase):

    def setUp(self):
        global driver

        opt = webdriver.ChromeOptions()
        opt.add_argument("--disable-notifications")
        opt.add_argument('--disable-blink-features=AutomationControlled')
        # opt.add_argument('--enable-javascript')
        driver = webdriver.Chrome(options=opt)

        driver.get("https://www.hotfrog.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_NestedFrame(self):
        scrollXpath = "// a[text() = 'Abbeville']"
        scrollElement = driver.find_element_by_xpath(scrollXpath)

        action = ActionChains(driver)
        action.move_to_element(scrollElement).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='aswift_1']"))

        titleHeading = "//div[@id='mys-wrapper']/descendant::a[2]"
        titleElement = driver.find_element_by_xpath(titleHeading)
        print(titleElement.text)

        # driver.switch_to.frame()

        # time.sleep(2)

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@frameborder='0']"))
        url = driver.find_element_by_xpath("//script[@type='text/javascript']")
        srcvalue= url.get_attribute("src")
        print(srcvalue)
        driver.get(srcvalue)

        pagesource = driver.page_source.count(str('this'))
        print(pagesource)

        # AllWindowHandle = driver.window_handles
        # driver.switch_to.window(AllWindowHandle[0])

        # tank = driver.find_element_by_xpath("//pre")
        # tank = driver.find('this')
        #
        #
        # for word in tank:
        #
        #      if word.text == 'this':
        #          print((word.text).count())

    def tearDown(self):
        time.sleep(5)
        driver.close()

unittest.main()