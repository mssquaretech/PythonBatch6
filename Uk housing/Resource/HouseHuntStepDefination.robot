*** Settings ***
Documentation    Suite description
Library         SeleniumLibrary
Resource        ..//Resource/Pages/HouseHuntPages.robot

*** Keywords ***
I navigate to HouseHunt.com
    open browser    https://househunt.london.ac.uk/         chrome
    maximize browser window
    capture page screenshot
    Load

I click to Find Your Property
    user click on find property

I switch to New Window
    user switch to New Window

I click on Search on New opened window
    user click on Search link

I select 1st Filter
    user click on 1st dropdown
    user select required option

I select 2nd Filter
    user click on Campus dropdown
    user select value from Campus dropdown

I click on See results
    user click on Search results

I get list of properties
    user gets list of properties

I sort properties from Low to high
    user click on default filter
    user sorted price

I print the names of first 5 properties
    print first 5 properties

