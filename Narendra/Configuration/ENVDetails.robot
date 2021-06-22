*** Settings ***
Library                     SeleniumLibrary

*** Variables ***
${URL}                      https://www.solihullsfc.ac.uk/

*** Keywords ***
Open the Webpage
    Open Browser            ${URL}          Chrome
    Maximize Browser Window

Close the Webpage
    Close all browsers