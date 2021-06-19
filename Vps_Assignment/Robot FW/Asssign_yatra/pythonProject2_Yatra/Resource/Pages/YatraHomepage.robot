*** Settings ***

#Documentation               Suite description
Library                     SeleniumLibrary
#Resource                ../Resource/YatraSD.robot

*** Variables ***

${RoundTrip}                    //a[@title='Round Trip']
${DepartCity}                   //input[@name='flight_origin' and @id='BE_flight_origin_city']
${DcityDropdownResult}          //p[@class='ac_cityname']/span[text()='(DEL)']
${GoingCity}                    //input[@name='flight_destination' and @id='BE_flight_arrival_city']
${GcityDropdownResult}          //strong[text()='Mumbai']
${DepartDate}                   //input[@name='flight_origin_date' and @id='BE_flight_origin_date']
${DepartDresult}                //td[@data-date='24/06/2021']
${ReturnDate}                   //input[@name='flight_destination_date']
${ResturnDateresult}            //td[@data-date='26/06/2021']
${NonStopcheck}                 //div[@class='filter-list']/a[@title='Non Stop Flights']/i
${TravellerClick}               //span[@class='txt-ellipses flight_passengerBox travellerPaxBox']
${TravellerCountIncrease}       //div[@data-flightagegroup='adult' and @class='pax-limit clearfix col-x-fluid']/div/div/span[@class='ddSpinnerPlus']
${SearchFlightButton}           //input[@value='Search Flights']

*** Keywords ***
#I navigate to Yatra
##    open browser                            https://yatra.com                   chrome
#    page should contain                         Flights
click on Round Trip
    click element                                   ${RoundTrip}
Enter Dcity
    sleep       1s
    input text                                      ${DepartCity}               Delhi
check some Suggestion
    sleep       2s
    click element                                   ${DcityDropdownResult}
Enter the Gcity
    sleep       2s
    input text                                      ${GoingCity}                Mumbai
Validate the First Suggestion
    sleep       1s
    click element                                   ${GcityDropdownResult}
Click on Depart Date
    click element                                   ${DepartDate}
Select the Date
    sleep       1s
    click element                                   ${DepartDresult}
Click on Return Date
    sleep       1s
    click element                                   ${ReturnDate}
Select the RDate
    sleep       1s
    click element                                   ${ResturnDateresult}
Select the Non Stop option
    click element                                   ${NonStopcheck}
Click on Traveller
    sleep       1s
    click element                                   ${TravellerClick}
Increase the Traveller Count
    sleep       1s
    click element                                   ${TravellerCountIncrease}
Click on Search button
    click element                                   ${SearchFlightButton}