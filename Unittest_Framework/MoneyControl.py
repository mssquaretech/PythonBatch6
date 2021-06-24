from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://moneycontrol.com")
driver.maximize_window()

srchBoxXpath = "//input[@id='search_str']"
srchElement = driver.find_element_by_xpath(srchBoxXpath)
srchElement.send_keys("RIL")
time.sleep (1)
srchFrstXpath = "//ul[@class='suglist scrollBar']/descendant::a"
time.sleep (2)
srchFrstElement = driver.find_element_by_xpath(srchFrstXpath)
srchFrstElement.click()

getValueElement = driver.find_element_by_id("nsespotval")
print("Share price of RIL is :", getValueElement.get_attribute('value'))

time.sleep(3)
scrollXpath = "//td[text()='OperatingProfit']"
scrollElement = driver.find_element_by_xpath(scrollXpath)

action = ActionChains(driver)
action.move_to_element(scrollElement).perform()


# AllwindowHandleList = driver.window_handles
# 1driver.switch_to.window(AllwindowHandleList[2])