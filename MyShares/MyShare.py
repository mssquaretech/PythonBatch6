from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("https://moneycontrol.com")

driver.maximize_window()

txtXpath = "//input[@class='txtsrchbox FL']"
txtElement = driver.find_element_by_xpath(txtXpath)
txtElement.send_keys('UTI Asset Management Company')
srchXpath = "//ul[@class='suglist scrollBar']/descendant::a[1]"
time.sleep(2)
srchElement = driver.find_element_by_xpath(srchXpath)
srchElement.click()
dsptext = "//div[@id='nsecp']"
txtPrint = driver.find_element_by_xpath(dsptext)
txt1 = "UTI Asset Management Company Ltd."
print(txt1, txtPrint.get_attribute('rel'))
txtXpath1 = "//form[@name='form_topsearch']/child::input[@id='search_str']"
txtElement1 = driver.find_element_by_xpath(txtXpath1)
txtElement1.send_keys('Indian Railway')
time.sleep(2)
srchXpath2 = "//a[contains(text(),'Indian Railway Finance Corporation')]"
time.sleep(2)
srchElement2 = driver.find_element_by_xpath(srchXpath2)
srchElement2.click()
dsptext2 = "//div[@id='nsecp']"
txtPrint1 = driver.find_element_by_xpath(dsptext2)
txt2 = "Indian Railway Finance Corporation Ltd."
print(txt2, txtPrint1.get_attribute('rel'))
time.sleep(2)
txtXpath2 = "//form[@name='form_topsearch']/child::input[@id='search_str']"
txtElement2 = driver.find_element_by_xpath(txtXpath2)
txtElement2.send_keys('Craftsman Automation')
srchXpath3 = "//a[contains(text(),'Craftsman')]"
time.sleep(2)
srchElement3 = driver.find_element_by_xpath(srchXpath3)
srchElement3.click()
dsptext3 = "//div[@id='nsecp']"
txtPrint2 = driver.find_element_by_xpath(dsptext3)
txt3 = "Craftsman Automation"
print(txt3, txtPrint2.get_attribute('rel'))
time.sleep(2)
driver.close()
