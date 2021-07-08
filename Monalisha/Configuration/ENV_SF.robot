*** Settings ***
Documentation                   Env file for salesforce testing
Library                         DateTime
Library                         String

*** Variables ***
${URL}                          https://d5g000005kxhheaw-dev-ed.my.salesforce.com/
${Browser}                      gc
${UserID}                       mssquareglobal1@gmail.com
${PWD}                          July@123
${FirstName}                    Monalisha_date
${LastName}                     Kar_date
${EmailID}                      mkar_date@gmail.com

*** Keywords ***
Create unique user details
    ${CurrentDate}      Get Current Date
    ${CurrentDate}      convert date    ${CurrentDate}          result_format=%y%m%d%H%M%S
    ${FirstName}        replace string  ${FirstName}        date      ${CurrentDate}
    ${LastName}         replace string  ${LastName}        date      ${CurrentDate}
    ${EmailID}          replace string  ${EmailID}        date      ${CurrentDate}
    set global variable     ${FirstName}
    set global variable     ${LastName}
    set global variable     ${EmailID}