*** Settings ***
Documentation    Suite description
Library                 SeleniumLibrary
Resource                Pages/Salesforce_Homepage.robot



*** Keywords ***
I navigate to Salesforce URL
    open browser            https://d5g000005kxhheaw-dev-ed.my.salesforce.com/          chrome
    maximize browser window


I Enter the Credentials "${USER}" and "${PASSWRD}"
    Enter the Credentials "${USER}" and "${PASSWRD}"

I Add new user
    Add New user


