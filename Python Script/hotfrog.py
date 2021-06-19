from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains

class hotfrog(unittest.TestCase):

    def setUp(self):

        global driver
        opt = webdriver.ChromeOptions()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument('--disable-notifications')
        opt.add_argument('--enable-javascript')
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        driver.get("https://www.hotfrog.com/")
        driver.implicitly_wait(10)

    def test_hotfrog(self):

        # addtextxpath = "//div[@class='row py-3']/descendant::div[starts-with(@class,'d-table-cell')]"
        # addtextelement = driver.find_elements_by_xpath(addtextxpath)
        #
        # for addtextname in addtextelement:
        #     print(addtextname.text)

        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//section[@class='container py-5']/div/div[@class='col-sm-4']/h2")).perform()

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='aswift_1']"))
        dataframe =driver.find_element_by_xpath("//div[contains(@id,'mys-content')]/descendant::a[contains(@data-asoch-targets,'titleClk') or contains(@data-asoch-targets,'ochTitle')]")
        print(" Ad frame Name :" + dataframe.text)

        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@frameborder='0']"))
        srcfile = driver.find_element_by_xpath("//script").get_attribute("src")
        print(srcfile)

        driver.get(srcfile)
        pagesource = driver.page_source.count('this')
        print("Count number of 'this' in srclink :" + str(pagesource))


        driver.switch_to.default_content()

if __name__ == '__main__':
        unittest.main()
