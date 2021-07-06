*** Settings ***
Library                             SeleniumLibrary
Resource                            ../Configuration/SFDC_env.robot


*** Variables ***
${TitleLogo}                        //img[@alt='Salesforce']
${Usernametextbox}                  //input[@id='username']
${Passwordtextbox}                  //input[@id='password']
${Loginbutton}                      //input[@id='Login']
${Setupsection}                     //div[@class='bLeft']//descendant::span[text()='Setup']


*** Keywords ***
Validate Salesforce URL Opened
    Log to console          ${\n}
    ${Title}                 Get Title
    Run Keyword If  '${Title}' == 'Login | Salesforce'
    ...     Log to console      Correct Salesforce URL opened.
    ...     ELSE    Fail    Incorrect URL opened.

Provide ${Username} and ${Password}
    input text         ${Usernametextbox}               ${Username}
    input text         ${Passwordtextbox}               ${Password}
    sleep   2s

Login with credential
    click element                       ${Loginbutton}
    Wait until element is Visible       ${Setupsection}         100s