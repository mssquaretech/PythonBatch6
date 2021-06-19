*** Settings ***
Library         SeleniumLibrary
Resource        YatraAdhoc.robot

*** Variables ***

${roundtrip}            //a[@title='Round Trip']
${FromCity}              BE_flight_origin_city
${ToCity}                BE_flight_arrival_city
${FromCityElement}      //p[contains(text(),'New Delhi')]
${ToCityElement}        //p[contains(text(),'Mumbai')]
${DeptCal}              //input[@id='BE_flight_origin_date']
${ArrCal}               //input[@id='BE_flight_arrival_date']
${DepDate}              //td[@data-date='25/06/2021']
${ArrDate}              //td[@data-date='26/06/2021']
${AdultCheckbox}        //span[contains(text(),'Adult')]/../following-sibling::div//span[@class='ddSpinnerPlus']
${EconomyClass}         //span[text()='Economy']/..
${NonStopFlight}        //a[@title='Non Stop Flights']/i
${SearchButton}         BE_flight_flsearch_btn
${SearchAgain}          //label[text()='Search Again']

*** Keywords ***
SelectRoundTrip
    click Element       ${roundtrip}
    sleep   2s
Select Dept City
    click Element       ${FromCity}
    sleep       2s
    click Element       ${FromCityElement}

Select Arrival City
    click Element       ${ToCity}
    sleep       2s
    click Element       ${ToCityElement}

Select Depature Date
    click Element       ${DeptCal}
    sleep       2s
    click Element       ${DepDate}

Select Return Date
    click Element       ${ArrCal}
    sleep       2s
    click Element       ${ArrDate}

Select 1 Adult
    Expand Traveller Economy
    click Element       ${AdultCheckbox}
#    CloseFrame


Check Econoy class
    click Element       ${EconomyClass}
    Expand Traveller Economy

Check NonStopFlights
    click Element       ${NonStopFlight}
Click on Search Button
    click Button        ${SearchButton}
    capture page screenshot

Validate Search result Loaded
    sleep   3s
    page should contain     ${SearchAgain}
    capture page screenshot
#Return flight list
#      Print List of Flights
#      Log     List is




