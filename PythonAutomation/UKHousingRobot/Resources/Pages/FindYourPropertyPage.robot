*** Settings ***
Library                                 SeleniumLibrary

*** Variables ***
${SearchButton}                         //aside//descendant::a[text()='Search']

*** Keywords ***
Validate New Window 'Find Your Property' Opened
    Switch Window                       NEW
    Page Should Contain                 Find Your Property

Click on 'Search' option
    Click Element                       ${SearchButton}