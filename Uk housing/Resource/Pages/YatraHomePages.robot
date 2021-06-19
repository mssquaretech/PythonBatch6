*** Settings ***
Library             SeleniumLibrary

*** Variables ***
${Roundtrip}                            //a[@title='Round Trip']
${StartDate}                            (//tbody[@class="BE_flight_origin_date"])[2]//following-sibling::tr[1]//td[@data-date="24/06/2021"]
${Origin}                               //input[@id='BE_flight_origin_city']
${OriginSuggestion}                     //li[@class='active ac_over']/descendant::span[1]
${Destination}                          //input[@id='BE_flight_arrival_city']
${DestinationSuggestion}                //li[@class='active ac_over']/descendant::p
${DepatureDate}                         //input[@name='flight_origin_date']
${returnDate}                           //td[@data-date='26/06/2021']
${travellerLabel}                       //label[@class='travellerLabel']
${PlusElement}                          (//span[@class='ddSpinnerPlus'])[1]
${Checkbox}                             (//i[@class='ico ico-checkbox'])[1]
${SearchFlights}                        //input[@value='Search Flights']


*** Keywords ***
Load
    page should contain                                                 Hotels

user click on round Trip
    sleep   2s
    click Element                                   ${Roundtrip}


user click on Departure tab
    sleep   3s
    click element                                   ${Origin}
    input text                                      ${Origin}           Delhi

user get Departure Location suggestion
    sleep   2s
    page should contain Element                     ${OriginSuggestion}

user select Mumbai as Arrival Location
    sleep 3s
    input text                                      ${Destination}        Mumbai


user get Arrival Location suggestion
    sleep 2s
    page should contain Element                     ${DestinationSuggestion}
    click element                                   ${DestinationSuggestion}


user click on departure date
    click element                                   ${DepatureDate}

user select start date
    sleep   2s
    click element                                   ${StartDate}

user select return date
    sleep   2s
    click element                                   ${returnDate}

user click on travellers
    sleep   2s
    click element                                   ${travellerLabel}

user select adult 2
    sleep   2s
    click element                                   ${PlusElement}

user click on checkbox
    sleep   2s
    click element                                   ${Checkbox}

user click on search flights
    sleep   2s
    click element                                   ${SearchFlights}
