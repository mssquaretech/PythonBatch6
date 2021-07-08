*** Settings ***
Documentation                               Home page for salesforce

*** Variables ***
${CreateXpath}                              //a[@title = 'Create Menu']
${DropdownXpath}                            //a[@title = 'Create Menu']/lightning-icon
${WaitElementXpath}                         //div[contains(@class, 'visible positioned')]
${UserXpath}                                //a[@data-id = 'userCreateMenuItem']/descendant::span[text()= 'User']
${UserFrameXpath}                           //iframe[contains(@title, 'New User')]
${NewUserXpath}                             //h1[text() = 'New User']
${SaveXpath}                                //td[@id = 'topButtonRow']/input[@title= 'Save']
${UserCreatedFrame}                         //iframe[starts-with(@title, 'User:')]
${UserDetails}                              //h2[text()= 'User Detail']


*** Keywords ***
check for home page
    page should contain                     Home
    page should contain element             ${CreateXpath}
    ${PageTitle}                            get title
    log to console                          Page title is: ${PageTitle}

click on Create dropdown
    click element                           ${DropdownXpath}
    Wait Until Page Contains Element        ${WaitElementXpath}             10sec

click on User
    click element                           ${UserXpath}

check for User page
#    Wait Until Page Contains Element        ${NewUserXpath}                 20sec
    page should contain                     New User

fill the form
    select frame                            ${UserFrameXpath}
    Wait Until Page Contains Element        ${NewUserXpath}                 20sec
    input text                              id:name_firstName               ${FirstName}
    input text                              id:name_lastName                ${LastName}
    input text                              id:Email                        ${EmailID}
    click element                           ${SaveXpath}
    unselect frame

user created
    wait until element is enabled           ${UserCreatedFrame}       30sec
    select frame                            ${UserCreatedFrame}
    page should contain element             ${UserDetails}
    log to console                          User created successfully

