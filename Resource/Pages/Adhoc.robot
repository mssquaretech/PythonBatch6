*** Settings ***
Library                                     OperatingSystem
Library                                     SeleniumLibrary
Library                                     DateTime

*** Keywords ***
LoadPageStrategy
    Execute JavaScript                       window.stop()
Generate ScreenShots
    ${CurrentDateTime}                       get current date
    ${CurrentDateTime}                       convert date       ${CurrentDateTime}          result_format=%y%m%d%H%M%S
    create directory                         ${CURDIR}/../../Results/ScreenShots_${CurrentDateTime}
    set screenshot directory                 ${CURDIR}/../../Results/ScreenShots_${CurrentDateTime}

