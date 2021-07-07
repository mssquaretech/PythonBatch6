*** Settings ***
Library                     SeleniumLibrary

*** Variables ***
${URL}                      https://d5g000005kxhheaw-dev-ed.my.salesforce.com/
${Browser}                  Chrome

*** Keywords ***
Open Salesforce page
    Open Browser            ${URL}              ${Browser}
    maximize browser window