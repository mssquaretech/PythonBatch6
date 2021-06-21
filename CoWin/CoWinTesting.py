from selenium import webdriver
from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.cowin.gov.in/home")

txtXpath = "//input[@id='mat-input-0']"

txtElement = driver.find_element_by_xpath(txtXpath)

txtElement.send_keys('422211')

srchXpath = "//button[contains(text(),'Search')]"

txtElement1 = driver.find_element_by_xpath(srchXpath)

txtElement1.click()

ageXpath = "//label[text()=' Age 45+ ']"

txtElement2 = driver.find_element_by_xpath(ageXpath)

txtElement2.click()

time.sleep(2)

OperatingXpath = "(//div[@class='row']/following-sibling::div)[2]"

OperatingElement = driver.find_element_by_xpath(OperatingXpath)

action = ActionChains(driver)

action.move_to_element(OperatingElement).perform()

hosTitle = "//h5[@class='center-name-title']"

statusBooked = "//a[starts-with(text(),' Booked ')]"

txtElement3 = driver.find_elements_by_xpath(hosTitle)

txtElement4 = driver.find_elements_by_xpath(statusBooked)

print(txtElement3[0].text)

print(txtElement4[0].text)

print(txtElement3[1].text)

print(txtElement4[1].text)
#
# hosTitle1 = "(//h5[@class='center-name-title'])[2]"
#
# txtElement5 = driver.find_element_by_xpath(hosTitle1)
#
# print(txtElement5.text)
#
# print(txtElement4.text)
