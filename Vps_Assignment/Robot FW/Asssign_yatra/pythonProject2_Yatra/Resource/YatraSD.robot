
*** Settings ***
#Documentation           Yatra Suite description
Library                         SeleniumLibrary
Resource                Pages/YatraHomepage.robot

*** Keywords ***
I navigate to Yatra.com
    open browser            http://www.yatra.com            chrome
    maximize browser window
I click on Round Trip
    click on Round Trip
I Enter the Depart City
     Enter Dcity
I get Some Suggestion
    check some Suggestion
I Click on Going To Form City
    Enter the Gcity
I Validate the Going option
    Validate the First Suggestion
I Check the Depart Date
    Click on Depart Date
I Select the Depart Date
    Select the Date
I Check the Return Date
    Click on Return Date
I Select the Return Date
    Select the RDate
I Select the Non Stop Otion
    Select the Non Stop option
I Validate the Traveller Count
    Click on Traveller
I Selct the Traveller Count
    Increase the Traveller Count
I Click on Search Flight option
    Click on Search button

#I Enter the Value in Depart From
#    Enter the Depart City
#I get Some Suggestion
#    Click on Going To Form text
#I Enter the Value in Going To
#    Enter teh Going To City
#Validate the Going option
#    Click on First Suggestion
#Check the Depart Date
#    Select the Depart Date
#I Select the Return Date
#    Select the DeReturn Date
#I Select the Non Stop Flight
#    Click on Non Stop
#I select the Traveller Count
#    Select the Traveller Count
#I Click on Search Flights
#    Click on Search Flight button
#
#Enter the Depart City
#    Input Text
#I get Some Suggestion
#    Click on Suggestion
#Click on Going To Form text
#    Enter the Going To City
#Validate the Going option
#    Click on First Suggestion
#Check the Depart Date
#    Select the Depart Date
#Check the Return Date
#    Select the Return Date
#Select the Non Stop Otion
#    Click on Non Stop
#Validate the Traveller Count
#    Click on Traveller dropdown
#Select the Traveller Count
#    Select the Traveller Count
#Click on Search Flight option
#    Click on Search Flight button




