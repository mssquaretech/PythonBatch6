from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://moneycontrol.com")

txtXpath ="//input[@class='txtsrchbox FL']"

txtElement = driver.find_element_by_xpath(txtXpath)

txtElement.send_keys("RIL")

srchResultXpath= "//div[@class='top_asugscrl']/child::ul/descendant::a"

time.sleep(2)

srchElementXpath = driver.find_element_by_xpath(srchResultXpath)

srchElementXpath.click()

txtprint = "//div[@id='nsecp']"

displayXpath = driver.find_element_by_xpath(txtprint)

print(displayXpath.get_attribute('rel'))

OperatingXpath = "//td[text()='OperatingProfit']"

operatingElement = driver.find_element_by_xpath(OperatingXpath)

action = ActionChains(driver)
action.move_to_element(operatingElement).perform()

