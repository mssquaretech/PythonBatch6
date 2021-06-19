*** Settings ***
Resource                Page/YatraHomePage.robot
Library                 SeleniumLibrary


*** Keywords ***

#I navigate to "${URL}" home page
#    Open Browser        ${URL}               chrome
#    maximize browser window
#    Page Load

I navigate to yatra.com home page
    [Arguments]         ${URL}               ${BROWSER}
    Open Browser        ${URL}               ${BROWSER}
    maximize browser window
    Page Load

I select road trip from delhi to mumbai
    Select origin flight city name
    Select destination city name

I select dep date as 24th June and return date 26th June
    Select depature date
    Select return date

I select for 2 adult with economy class
    Select number of traveller

I mark for non stop flight
    Select non stop flight

I click on submit button
    click submit button

I get result for only non stop flight for mention date and destination
    All filghts got requested inputs