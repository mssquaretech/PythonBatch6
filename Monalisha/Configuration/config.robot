*** Settings ***
Library                 OperatingSystem
Library                 DateTime

*** Keywords ***
Generate screenshot directory
    ${CurrentDateTime}              get current date
    ${CurrentDateTime}      convert date        ${CurrentDateTime}      result_format=%y%m%d%H%M%S
    create directory                ${CURDIR}/../Results/Screenshot_${CurrentDateTime}
    set screenshot directory        ${CURDIR}/../Results/Screenshot_${CurrentDateTime}

close current browser
    Close Browser
