from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://moneycontrol.com")

searchXpath = "//input[@class='txtsrchbox FL' and @id='search_str']"

searchXpath = driver.find_element_by_xpath(searchXpath)

searchXpath.send_keys("RIL")

time.sleep(5)

#searchResultXpath="//a/child::span[text()='INE002A01018	, RELIANCE	, 500325	']"

searchResultXpath="//div[@class='top_asugscrl' and @id='autosuggestlist']/descendant::a[starts-with(text(),'Reliance Industries')]/child::span"

searchResultElement = driver.find_element_by_xpath(searchResultXpath)

searchResultElement.click()
CheckResultXpath = "//div[@id='nsecp']"


#//div[@class='indimprice']/div[@id='nsecp']/ #data-numberanimate-value="1,987.95"

CheckNseXpath = driver.find_element_by_xpath(CheckResultXpath).get_attribute("data-numberanimate-value")

print(CheckNseXpath)


