from selenium import webdriver
from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.moneycontrol.com")

TopSearch = "//form[@name='form_topsearch']/input[@id='search_str']"

TopSearchElement = driver.find_element_by_xpath(TopSearch)
TopSearchElement.send_keys("RIL")

time.sleep(2)

InputSearch = "//div[@class='top_asugscrl']/ul[contains(@class,'scrollBar')]/li[1]/a"
InputElement = driver.find_element_by_xpath(InputSearch)
InputElement.click()

RilValuePath = "//input[@id='nsespotval']"
RilValueElement = driver.find_element_by_xpath(RilValuePath)

print(RilValueElement.get_attribute('value'))

time.sleep(3)

ScrollToVariable = "//table[@class='frevdat']/tbody/tr[3]/td"
ScrollElement = driver.find_element_by_xpath(ScrollToVariable)

action = ActionChains(driver)
action.double_click(ScrollElement).perform()


