*** Settings ***
Library                     SeleniumLibrary
Resource                    ../Configuration/Details.robot
Resource                    ../Resources/AmazonHomePage.robot

*** Keywords ***
I Open Amazon Home Page
    Open Browser            ${AmazonURL}          chrome
    Maximize Browser Window

I Select to Category
    Click on Amazon Category Drop Down

I Click all Category
    ${Result}=  Click on All Category from Drop Down
    [Return]    ${Result}

I Print only Five category
    [Arguments]     ${Results}
    Print the first five category only      ${Results}