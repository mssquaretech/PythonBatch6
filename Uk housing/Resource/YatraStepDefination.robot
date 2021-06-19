*** Settings ***
Library     SeleniumLibrary
Resource        ..//Resource/Pages/YatraHomePages.robot

*** Keywords ***
I navigate to Yatra.com website
    open browser        https://www.yatra.com       chrome
    maximize browser window
    capture page screenshot
    Load

I select Round trip flights from Delhi to Mumbai
    user click on round Trip
    user click on Departure tab
    user get Departure Location suggestion
    user select Mumbai as Arrival Location
    user get Arrival Location suggestion


I select Departure Date and return Date
    user click on departure date
    user select start date
    user select return date

I select number on Adults
    user click on travellers
    user select adult 2

I Mark checkbox for Non-Stop flights
    user click on checkbox

I will get list of flights
    user click on search flights
    user will get flight details

