*** Settings ***
Library                         SeleniumLibrary
Resource                        ../Configurations/Browser.robot
Resource                        Pages/UKpage1.robot
Resource                        Pages/UKpage2.robot


*** Keywords ***
I navigate to
    [Arguments]             ${URL}              ${BROWSER}
    open browser            ${URL}              ${BROWSER}
    maximize browser window
    Set Selenium Implicit Wait                   20sec

I check for correct page open
    page should contain                         Find Your Property


I search for property
    find property

I switch to new tab
    go to new tab
    check new window opened

I click on search
    search property

I fill dropdown with values
    select University
    select campus

I click on See result
    see result

I wait for result to be loaded
    wait till result appear

I sort properties as Low to High
    sort low to high

I print the first five proporties
    wait till result appear
    print property

