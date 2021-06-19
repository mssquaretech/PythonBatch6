from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

xpath = "//input[@name='q']"

InputBox = driver.find_element_by_xpath(xpath)

InputBox.send_keys("Python")

SelectList = "//div[@role='option']/div/span"

time.sleep(2)

SelectListElement = driver.find_element_by_xpath(SelectList)

SelectListElement.click()