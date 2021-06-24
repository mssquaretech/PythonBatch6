from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

txtBoxXPth = "//input[@name='q']"
txtBxElement = driver.find_element_by_xpath(txtBoxXPth)
txtBxElement.send_keys("Amazon")

searchELemet = "//ul[@class = 'erkvQe']/descendant::span"
time.sleep(3)
createElement = driver.find_element_by_xpath(searchELemet)

createElement.click()

amazonXpath = "//div[@class='uEierd']/descendant::span[contains(text(),'http://www.amazon.in/')]"
time.sleep(3)
amazonElement = driver.find_element_by_xpath(amazonXpath)
amazonElement.click()

time.sleep(2)
signInElement = driver.find_element_by_id("nav-link-accountList")
signInElement.click()

loginIDXpath = "//input[@id = 'ap_email']"
time.sleep(1)
loginIDelement = driver.find_element_by_xpath(loginIDXpath)
loginIDelement.send_keys("monalishakar.92@gmail.com")
continueButtXpath = "//input[@id = 'continue']"
time.sleep(1)
continueButtElemet = driver.find_element_by_xpath(continueButtXpath)
continueButtElemet.click()