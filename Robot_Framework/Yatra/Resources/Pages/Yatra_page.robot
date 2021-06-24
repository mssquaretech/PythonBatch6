*** Settings ***
Library                             SeleniumLibrary

*** Variables ***

${RoundTrip}                           //a[@title = 'Round Trip']
${OriginCity}                           //input[@id= 'BE_flight_origin_city']
${OriginCityselect}                     //div[@class= 'viewport']/descendant::p[contains(text(), 'New Delhi')]
${DestCity}                             //input[@id= 'BE_flight_arrival_city']
${DestCitySelect}                       //span/strong[text() = 'Mumbai']
${DepDatebox}                           //input[@id= 'BE_flight_origin_date']
${DepDateSelect}                        //td[@id = '24/06/2021']
${ReturnDatebox}                        //input[@id= 'BE_flight_arrival_date']
${ReturndateSelect}                     //td[@id = '26/06/2021']
${Traveller}                            //span[text() = 'Traveller']
${AdultSelect}                          //span[@class = 'ddSpinnerPlus']
${FrameEle}                             //i[@class = 'we_forward']
${NonSTopbox}                           //a[@title= 'Non Stop Flights']/i
${SearchBox}                            //input[@id = 'BE_flight_flsearch_btn']



*** Keywords ***
page check
    page should contain                    Flights

Round trip
    click element                          ${RoundTrip}

Origin check
    click element                           ${OriginCity}
    input text                              ${OriginCity}                          Delhi
    page should contain                     New Delhi
    Wait Until Element Is Visible           ${OriginCityselect}
    click element                           ${OriginCityselect}
    sleep                                   2sec

Destination check
    click element                           ${DestCity}
    input text                              ${DestCity}                            Mumbai
    sleep                                   2sec
    page should contain                     Mumbai
    sleep                                   2sec
    click element                           ${DestCitySelect}

Date select
    page should contain                     Departure Date
    click element                           ${DepDatebox}
    click element                           ${DepDateSelect}
    page should contain                     Return Date
    click element                           ${ReturnDatebox}
    click element                           ${ReturndateSelect}

traveller select
    click element                           ${Traveller}
    page should contain                     Adult
    click element                           ${AdultSelect}
    select frame                            id:webklipper-publisher-widget-container-notification-frame
    Current Frame Should Contain            A note of advice
    click element                           ${FrameEle}
    Unselect Frame

nonstop
    click element                           ${NonSTopbox}

Search Flight
    click element                           ${SearchBox}









