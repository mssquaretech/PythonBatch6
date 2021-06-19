*** Settings ***
Library                         SeleniumLibrary
Resource                        ../Configuration/Details.robot
Resource                        Pages/MainPage.robot
Resource                        Pages/FindYourPropertyPage.robot
Resource                        Pages/PropertySearchPage.robot


*** Keywords ***
I Open the Housing Property Website of 'University of London'
    Open Browser                ${URL}                              chrome
    Maximize Browser Window

I Navigate and open the 'Find Your Property' section
    Navigate and open the 'Find Your Property' option
I Open the 'Search' section
    Validate New Window 'Find Your Property' Opened
    Click on 'Search' option
I Select the 'University' and 'Campus'
    Validate New Search Page Opened
    Select 'University' and 'Campus' from Drop Down
I Search the Property
    Click on Search Button
    Validate the result of properties display
I Sort the property pricing with 'Low to High'
    Click on Sorting Button
    Select the Price: Low to High
    Wait till new Property List display
I Capture and print the names of first 5 Properties
    Capture the total Properties Display and Initiate Loop to display Properties