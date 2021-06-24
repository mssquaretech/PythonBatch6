*** Settings ***
Resource                                Pages/Yatra_page.robot
Resource                                Pages/Yatra_page2.robot


*** Keywords ***
I navigate to URL
    [Arguments]                     ${URL}           ${Browser}
    open browser                        ${URL}                  ${Browser}
    maximize browser window
    Set Selenium Implicit Wait              20sec

I check Yatra page is opened
    page check

I search for Round trip flight
    Round trip

I select flight from Delhi to Mumbai
    Origin check
    Destination check

I select departure and return date
    Date select

I select 2 Adults of Economy class
    traveller select

I select non-stop flight
    nonstop

I search to get the flight list
    Search Flight

I check the Flight list
    list check