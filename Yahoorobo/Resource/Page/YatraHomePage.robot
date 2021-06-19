*** Settings ***
Library                            SeleniumLibrary
Library                            ../../Library/Iframeclose.py

*** Variables ***
${clickInputOrigion}                //input[@id='BE_flight_origin_city']
${selectDropdown}                   //div[@class='ac_airport']/p
${clickInputdestination}            //input[@name='flight_destination']
${clickdepatureDate}                //input[@id='BE_flight_origin_date']
${clickreturnDate}                  //input[@id='BE_flight_arrival_date']
${selecdepatureDate}                //td[@id='24/06/2021']
${selecreturnDate}                  //td[@id='26/06/2021']
${travellerselection}               //label[@class='travellerLabel']
${clickOnAddTraveller}              //span[@class='ddSpinnerPlus']
${nostopclick}                      //a[@for='BE_flight_non_stop']
${Submit}                           //input[@type='submit']

*** Keywords ***
Page Load
    page should contain              Yatra

Select origin flight city name
    Click Element                    ${clickInputOrigion}
    Sleep                            3
    Input Text                       ${clickInputOrigion}             Delhi
    Sleep                            3
    Page Should Contain Element      ${selectDropdown}
    Click Element                    ${selectDropdown}

Select destination city name
    Click Element                    ${ClickInputdestination}
    Sleep                            3
    Input Text                       ${ClickInputdestination}           Bom
    Sleep                            3
    Page Should contain Element      ${selectDropdown}
    Click Element                    ${selectDropdown}
    Sleep                            2

Select depature date
    Click Element                   ${clickdepatureDate}
    Sleep                           2
    Click Element                   ${selecdepatureDate}

Select return date
    Sleep                           3
    Click Element                   ${clickreturnDate}
    Sleep                           2
    Click Element                   ${selecreturnDate}

Select number of traveller

    Click Element                   ${travellerselection}
    Sleep                           2
    Click Element                   ${clickOnAddTraveller}
    Click Element                   ${travellerselection}
    Sleep                           2
    iframeclose

Select non stop flight
    ClickElement                    ${nostopclick}
    Sleep                           2

click submit button
    ClickElement                    ${Submit}

All filghts got requested inputs
    Page should contain             Book Now