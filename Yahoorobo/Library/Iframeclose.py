from selenium import webdriver

def iframeclose(self):

        driver = webdriver.Chrome()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='webklipper-publisher-widget-container-notification-frame']"))
        driver.find_element_by_xpath("//div[@class='tablecell minimize']").click()
        driver.switch_to.default_content()