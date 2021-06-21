from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

txtXpath = "//input[@type='text']"

txtElement = driver.find_element_by_xpath(txtXpath)

txtElement.send_keys("automation")

searchResultXpath = "//div[@class='wM6W7d']/span[text()='automation']"

time.sleep(5)

searchElementXpath = driver.find_element_by_xpath(searchResultXpath)

searchElementXpath.click()

driver.close()