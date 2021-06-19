from selenium import webdriver

Rediff = webdriver.Chrome()
Rediff.get("https://www.rediff.com/news")
Rediff.maximize_window()

NewsXpath = "(//div[contains(@class, 'secstorybox')]/h2)"
NewsCountElement = len(Rediff.find_elements_by_xpath(NewsXpath))

for a in range(NewsCountElement):
    a += 1
    NewsText = "(//div[contains(@class, 'secstorybox')]/h2)["
    NewsText += str(a)
    NewsText += "]/a"

    NewsTextXpath = Rediff.find_element_by_xpath(NewsText)
    print("News are :{}".format(NewsTextXpath.text))

