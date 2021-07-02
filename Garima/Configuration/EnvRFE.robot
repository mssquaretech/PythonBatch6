*** Settings ***
Library                     SeleniumLibrary
Library                     OperatingSystem
Library                     DateTime

*** Variables ***
${URL}                      https://www.w3schools.com/howto/howto_css_contact_form.asp
${Browser}                  gc
${NumOfEntries}             5


*** Keywords ***
PreRequisite
    ${CurrentDateTime}              get current date
    ${CurrentDateTime}              convert date    ${CurrentDateTime}      result_format=%y%m%d%H%M%S
    create directory                ${CURDIR}/../Results/ScreenShots_${CurrentDateTime}
    set screenshot directory        ${CURDIR}/../Results/ScreenShots_${CurrentDateTime}


Closure
    close all browsers