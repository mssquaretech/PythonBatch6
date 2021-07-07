*** Settings ***
Library                         SeleniumLibrary
Library                         DateTime

*** Variables ***
${UserspageURL}                 https://d5g000005kxhheaw-dev-ed.lightning.force.com/lightning/setup/ManageUsers/home
${NewUserbutton}                //td[@class='pbBottomButtons']/input[@value='New User']
${Userframe}                    //iframe[contains(@title,'Users ~ Salesforce')]
${Usersection}                  //div[@class='bLeft']//descendant::span[text()='Users']
${NewUserFrame}                 //iframe[contains(@title,'New User ~ Salesforce')]
${LastName}                     //input[@id='name_lastName']
${License}                      //option[text()='Salesforce']
${Role}                         //option[text()='Marketing Team']
${Profile}                      //option[text()='Marketing User']
${Save}                         //td[@class='pbButtonb']/child::input[contains(@value,'Save')]
${FrameafterUserCreation}       //iframe[contains(@title,'Salesforce - Developer')]
${UserCreated}                  //div[@class='bPageTitle']//descendant::h2


*** Keywords ***
Validate Users page is opened
    ${CurrentURL}       Get Location
    Run Keyword If  '${CurrentURL}' == '${UserspageURL}'
    ...     Log to console      Correct Salesforce Userpage opened.
    ...     ELSE    Fail    Incorrect Salesforce Userpage url opened.

Validate New User Creation Display
    Wait Until Element Is Visible       ${Userframe}            timeout=20s
    select frame                        ${Userframe}

Click on New User Button
    Wait Until Element Is Visible       ${NewUserbutton}        timeout=20s
    Click Element                       ${NewUserbutton}
    unselect frame

Validate New User Form Display
    Wait Until Element Is Enabled       ${NewUserFrame}         timeout=10s
    select frame                        ${NewUserFrame}

Provide all user details in Form
    ${CurrentDate}      Get Current Date
    ${CurrentDate}      convert date    ${CurrentDate}          result_format=%y%m%d%H%M%S
    Set Selenium Speed  0.5 seconds
    Input text                          name_firstName          Narendra_${CurrentDate}
    Input text                          name_lastName           Shakya_${CurrentDate}
    Input text                          Email                   Naren${CurrentDate}@yopmail.com
    Input text                          Title                   Mr
    click element                       user_license_id
    click element                       ${License}
    click element                       role
    click element                       ${Role}
    click element                       Profile
    click element                       ${Profile}
    execute javascript                  window.scrollTo(0,document.body.scrollHeight)

Submit the user creation form
    click element                       ${Save}
    unselect frame

Validate new user created successfully
    wait until element is enabled       ${FrameafterUserCreation}       timeout=30s
    select frame                        ${FrameafterUserCreation}
    ${UsernameText}=    Get Text    ${UserCreated}
    ${source}=      Set Variable    ${UsernameText}
    ${contains}=    Run Keyword And Return Status    Should Contain    ${source}    Narendra
    Run Keyword If  "${contains}" == "True"
    ...     Log to console      User Created Successfully