from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class UKHousingPropTesting(unittest.TestCase):

    def setUp(self):
        global UKHousing
        UKHousing = webdriver.Chrome()
        UKHousing.get("https://househunt.london.ac.uk/")
        UKHousing.maximize_window()

    def test_UKHousingTesting(self):

        # Scroll down to bottom of the Page to select "Find Your Property".

        BottomPageXpath = "//div[contains(text(),'rights')]"
        BottomPageXpathElement = UKHousing.find_element_by_xpath(BottomPageXpath)
        Scroll = ActionChains(UKHousing)
        Scroll.move_to_element(BottomPageXpathElement).perform()

        # Sometimes it scrolled to "New Properties" section by itself.
        # So it will check and scroll back to the bottom of the Page.

        NewPropertiesXpath = "//h3[text()='New Properties']"
        NewPropertyVisible = WebDriverWait(UKHousing, 50).until(
            EC.presence_of_element_located((By.XPATH, NewPropertiesXpath)))
        if NewPropertyVisible.is_displayed():
            BottomPageXpath = "//div[contains(text(),'rights')]"
            BottomPageXpathElement = UKHousing.find_element_by_xpath(BottomPageXpath)
            AgainScroll = ActionChains(UKHousing)
            AgainScroll.move_to_element(BottomPageXpathElement).perform()
        else:
            pass

        FindYourPropXpath = "//div[@class='col-footer']//descendant::a[text()='Find Your Property']"
        FindYourPropXpathElement = UKHousing.find_element_by_xpath(FindYourPropXpath)
        FindYourPropXpathElement.click()

        # New Window will be opened after clicking the "Find Your Property".
        # Switch to new window and click on Search option.

        ListofWindow = UKHousing.window_handles
        UKHousing.switch_to.window(ListofWindow[1])

        SearchLinkXpath = "//aside//descendant::a[text()='Search']"
        SearchLinkXpathElement = UKHousing.find_element_by_xpath(SearchLinkXpath)
        SearchLinkXpathElement.click()

        # New Link will be open on same window.
        # Select all required drop down options with the help of Explicit Wait.
        # Click on Search button.

        UniverscityButton = "//div[text()=' University ']"
        UniverscityButtonElement = UKHousing.find_element_by_xpath(UniverscityButton)
        UniverscityButtonElement.click()

        RAMXpath = "//span[contains(text(),'RAM')]"
        WebDriverWait(UKHousing, 3).until(EC.element_to_be_clickable((By.XPATH, RAMXpath)))
        RAMXpathElement = UKHousing.find_element_by_xpath(RAMXpath)
        RAMXpathElement.click()

        CampusButton = "//div[text()=' Campus ']"
        CampusButtonElement = UKHousing.find_element_by_xpath(CampusButton)
        CampusButtonElement.click()

        MainCampus = "//span[text()='Main Campus']"
        WebDriverWait(UKHousing, 3).until(EC.element_to_be_clickable((By.XPATH, MainCampus)))
        MainCampusElement = UKHousing.find_element_by_xpath(MainCampus)
        MainCampusElement.click()

        SearchButton = "//button[text()='See Results']"
        SearchButtonElement = UKHousing.find_element_by_xpath(SearchButton)
        SearchButtonElement.click()

        # Explicit Wait till the results display.

        Results = "//div[@class='row search-result']/child::p[text()=' results ']"
        WebDriverWait(UKHousing, 50).until(EC.presence_of_element_located((By.XPATH, Results)))

        # Sort the list of properties price Low to High.

        PriceButtonXpath = "//span[text()='Default']"
        PriceButtonXpathElement = UKHousing.find_element_by_xpath(PriceButtonXpath)
        PriceButtonXpathElement.click()

        LowToHighXpath = "//span[text()='Price: Low to High']"
        WebDriverWait(UKHousing, 5).until(EC.presence_of_element_located((By.XPATH, LowToHighXpath)))
        LowToHighXpathElement = UKHousing.find_element_by_xpath(LowToHighXpath)
        LowToHighXpathElement.click()

        # Explicit wait till the refresh is not completed.

        ResultButtonXpath = "//div[@class='submit-group']//child::button[@class='btn btn-lg btn-primary--hover']"
        WebDriverWait(UKHousing, 50).until(EC.presence_of_element_located((By.XPATH, ResultButtonXpath)))

        # Count the Total Properties listed.

        TotalProperties = "//div[@class='row search-result']//child::div[@class='row']//descendant::h3"
        TotalCount = len(UKHousing.find_elements_by_xpath(TotalProperties))

        # Initialize the For Loop on listed properties.

        print("Top 5 Properties are:")

        x = 1
        for a in range(1, TotalCount):
            Xpath = "//div[@class='row search-result']//child::div[@class='row']//descendant::h3["
            Xpath += str(x)
            Xpath += "]"
            XpathElement = UKHousing.find_element_by_xpath(Xpath)

            """
            Increment the index value by 2 to display the property name only,
            else it will consider the City/State also.
            Increment will run only till the 2nd Last list of property,
            else it will increase the index value(out of index) which will fails to locate the element. 
            """

            if x < TotalCount - 1:
                x = x + 2
            else:
                pass

            # Print only top 5 Properties

            if a <= 5:
                print("{}. {}".format(a, XpathElement.text))
            else:
                pass


if __name__ == "__main__":
    unittest.main()