from selenium import webdriver

CoWinner = webdriver.Chrome()
CoWinner.get("https://www.cowin.gov.in/home")
CoWinner.maximize_window()

# Enter PIN Code
Pincodepath = "//input[contains(@placeholder,'Enter your PIN')]"
PincodeElement = CoWinner.find_element_by_xpath(Pincodepath)
PincodeElement.send_keys("110007")

# Click on Search
Searchpath = "//button[text()=' Search ']"
SearchElement = CoWinner.find_element_by_xpath(Searchpath)
SearchElement.click()

# Click on Age Limit above 45
Agepath = "//label[text()=' Age 45+ ']"
AgeElement = CoWinner.find_element_by_xpath(Agepath)
AgeElement.click()

# Count the Total occurrence  of Hospital Row
TotalRow = "(//div[@class='center-box']/descendant::div[@class='row'])"
RowCount = len(CoWinner.find_elements_by_xpath(TotalRow))
print('Total number of Hospitals available : {}'.format(RowCount))
print()
print("Below Hospitals are Booked:")

# For loop till the occurrence of Hospital row
for a in range(RowCount):
    a = a + 1
    # Passing the Variable count in Xpath by concatenating the Hospital Xpath
    # Getting the Xpath of Hospital's name
    HospitalXpath = "(//div[@class='center-box']/descendant::div[@class='row'])["
    HospitalXpath += str(a)
    HospitalXpath += "]/descendant::h5"
    HospitalXpathElement = CoWinner.find_element_by_xpath(HospitalXpath)

    # Getting the Hospital's Booking status by again using concatenation
    BookingStatus = HospitalXpath
    BookingStatus += "/ancestor::div[starts-with(@class,'main-slider')]/following-sibling::div/child::ul/li/div/div/a"
    BookingElement = CoWinner.find_element_by_xpath(BookingStatus)

    # Checking the Booking status and printing only the Hospital which are booked
    if BookingElement.text == "Booked":
        print("Hospital Name: {}".format(HospitalXpathElement.text))
        print("Booking Status is:  {}".format(BookingElement.text))
        print()
    else:
        pass

CoWinner.close()