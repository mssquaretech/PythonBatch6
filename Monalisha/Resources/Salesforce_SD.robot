*** Settings ***
Documentation                               Step Definition file for Salesforce testing
Resource                                    Pages/Salesforce_Page1.robot
Resource                                    Pages/Salesforce_Homepage.robot
Library                                     SeleniumLibrary


*** Keywords ***
I navigate to
        [Arguments]                         ${url}                  ${browser}
        open browser                        ${url}                  ${browser}
        maximize browser window
        capture page screenshot
        Set Selenium Implicit Wait          20sec

I check Salesforce page is opened
        login page check

I provide credential to login
        [Arguments]                         ${USER}                 ${Pwd}
        set global variable                 ${USER}
        set global variable                 ${Pwd}
        Login action

I check Home page is opened
        check for home page

I try to create New user with
        [Arguments]             ${FName}        ${LName}            ${Email}
#        Create unique user details
        set global variable     ${FName}
        set global variable     ${LName}
        set global variable     ${Email}
        click on Create dropdown
        click on User
        check for User page
        fill the form

I check new user created
        user created
