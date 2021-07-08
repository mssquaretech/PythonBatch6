*** Settings ***
Documentation                           Login page for Salesforce

*** Variables ***
${Logo}                                 //img[@id = 'logo']

*** Keywords ***
login page check
    page should contain             salesforce
    page should contain element     ${Logo}

Login action
    input text                      id:username                         ${USER}
    input text                      id:password                         ${Pwd}
    click element                   id:Login
    Wait Until Page Contains        Home
