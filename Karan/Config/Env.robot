*** Settings ***
Library             SeleniumLibrary
Library             OperatingSystem
Library             DateTime

*** Variables ***


*** Keywords ***
Pre conditions for flow
        ${CurrentDate}                     get current date
        ${DictExtension}                   convert date      ${CurrentDate}        results_format=%y.%m.%d.%H%M%S
        Create Directory                   ${CURDIR}/../Result/Screenshot_${DictExtension}
        Set Screenshot Directory           ${CURDIR}/../Result/Screenshot_${DictExtension}
        Set Selenium Implicit Wait         10s

Close Browser
        Close All Browsers

