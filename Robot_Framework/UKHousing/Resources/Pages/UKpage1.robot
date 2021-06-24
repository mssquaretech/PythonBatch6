*** Settings ***
Documentation                   implementation of page 1
Library                         SeleniumLibrary

*** Variables ***
${findPropertyXpath}                            //li[@class = 'nav-item']/child::a[text() = 'Find Your Property']


*** Keywords ***
find property
    click element                               ${findPropertyXpath}

go to new tab
    Switch Window	                             NEW

check new window opened
    page should contain                          Home




