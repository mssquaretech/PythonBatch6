from selenium import webdriver

UKHousing = webdriver.Chrome()
UKHousing.get("https://househunt.london.ac.uk/")
UKHousing.maximize_window()