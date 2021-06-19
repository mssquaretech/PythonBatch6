*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     DateTime

*** Variables ***
${BROWSER}          chrome


*** Keywords ***

Getting screenshot under dict
    ${CURRENTDATETIME}              get current date
    ${FILEDATETIME}                 convert date     ${CURRENTDATETIME}      results_format=%y.%m.%d.%H.%M.%S
    create directory                ${CURDIR}/../Results/Screenshot_${FILEDATETIME}
    set screenshot directory        ${CURDIR}/../Results/Screenshot_${FILEDATETIME}

close browser
    close all browsers




