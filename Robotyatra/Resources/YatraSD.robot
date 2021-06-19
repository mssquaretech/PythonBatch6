*** Settings ***
Library                 SeleniumLibrary
#Library                 SeleniumLibrary.Set
#Library                 SeleniumLibrary.Get
Resource                Pages/YatraPage.robot
Library      SeleniumLibrary
Resource     Pages/YatraPage.robot
*** Keywords ***
I navigate to "${URL}" in webbrowser "${Browser}"
    #[Arguments]      ${URL}      ${Browser}
    open browser    ${URL}      ${Browser}
    maximize browser window
#    Set Selenium Implicit Wait 5
    sleep       3s
I select round trip
    SelectRoundTrip
I select City of Depature and Arrival
    Select Dept City
    Select Arrival City
I select Depature and Return dates
    Select Depature Date
    Select Return Date
I select number of Travellers
    Select 1 Adult
I select economy class
    Check Econoy class
I select NonStop Flights
    Check NonStopFlights
I click on Search Button
    Click on Search Button
I see list of flights
#    Validate Search result Loaded
#    Return flight list
    capture page screenshot