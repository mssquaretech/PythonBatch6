from selenium import webdriver

import time

driver = webdriver.Chrome()
driver.get("https://www.cowin.gov.in/home")

PinSearch = "//div[@class='pin-search']/input"
PinSearchElement = driver.find_element_by_xpath(PinSearch)
PinSearchElement.send_keys("226002")

time.sleep(3)

SearchButton = "//button[@class='pin-search-btn']"
SearchButtonElement = driver.find_element_by_xpath(SearchButton)
SearchButtonElement.click()

AgeSelect = "//label[contains (text(), '45+')]"
AgeSelectElement = driver.find_element_by_xpath(AgeSelect)
AgeSelectElement.click()

time.sleep(3)

CentralName = "//div[@class='row-disp']/h5"
HospStatus = "//span[@class='age-limit']/ancestor::div[contains (@class,'slots-box')]/div/a"

CentralNameElement = driver.find_elements_by_xpath(CentralName)
HostStatuslist = driver.find_elements_by_xpath(HospStatus)

print(CentralNameElement[1].text)
print(HostStatuslist[1].text)



