*** Settings ***
Library             SeleniumLibrary
Resource            Pages/HouseHuntPage.robot
Resource            Pages/Findoutpage.robot

*** Keywords ***

I navigate to "${URL}" using "${BROWSER}"
    open browser         ${URL}             ${BROWSER}
    maximize browser window
    set selenium implicit wait          10s
    PageLoad

I click on found out property link on Home Page
    Click on found out property
    Move to found out proprty window

I click on search section on new window
    Click on search

I select university and campus for search
    Select university
    Select campus

I get result for selected university campus
    Click Submit

I select for low to high price filter
    Selection of required filter

I print first "${linksRequired}" university
    Print required "${linksRequired}" of university Name