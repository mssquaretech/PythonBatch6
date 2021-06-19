from selenium import webdriver
import time

objname = webdriver.Chrome()
objname.get("https://www.google.com/")

boxpath = "//input[@class='gLFyf gsfi']"
Elementpath = objname.find_element_by_xpath(boxpath)
Elementpath.send_keys("Hello Monday")

time.sleep(4)
Searchresult = "(//div[@role='option' and @class='zRAHie']/div/span)[3]"
SearchElement = objname.find_element_by_xpath(Searchresult)
SearchElement.click()