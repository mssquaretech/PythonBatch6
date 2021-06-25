*** Settings ***
Documentation                       Step defination file for each Keyword of Feature file
Library                             SeleniumLibrary
Resource                            Pages/SoliHull_page.robot



*** Keywords ***
I navigate to "${site_URL}" in "${Browser}"
    open browser                    ${site_URL}                         ${Browser}
    maximize browser window
    capture page screenshot
    Set Selenium Implicit Wait                   20sec

I validate page title
    [Arguments]                                 ${HomePageTitle}
    Validate "${HomePageTitle}" is opened
    Validate page Logo

I click on top right corner dropdown
    click on right most dropdown

I print page title of selected languages starting with letter "${StartLetter}"
    count language starts with "${StartLetter}"
    select language and print page title




