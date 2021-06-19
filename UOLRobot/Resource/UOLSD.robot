*** Settings ***
Library         SeleniumLibrary
Resource        Pages/UOLHomePages.robot
Resource        Pages/UOLSearchPage.robot

*** Keywords ***
I Navigate to househunt webPage
    [Arguments]     ${URL}      ${Browser}
    open browser    ${URL}      ${Browser}
    maximize browser window
    capture page screenshot

I click on Find Your Property
#    Click on Menu find-your-property

    Click on Menu "find-your-property"

I see a new page launched
    Switch to new Tab

I Search My Properties
    Select Serch from Menu

UOL page Navigates to Search filter page
    Page contains filters

I apply search filters and click on Search
    [Arguments]     ${University}
    Select filters "${University}"
    Click on search

I see the list of properties
    List of properties returned

I Print "${Number}" from the list
    capture page screenshot
    print list "${Number}" of Properties

