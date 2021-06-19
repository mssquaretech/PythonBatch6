*** Settings ***
Library                                 SeleniumLibrary

*** Variables ***
${FindYourProperty}                     //a[text()='Find Your Property']

*** Keywords ***
Navigate and open the 'Find Your Property' option
    Click Element                       ${FindYourProperty}
