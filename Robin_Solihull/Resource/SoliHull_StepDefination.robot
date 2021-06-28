*** Settings ***
Resource                            Page/Solihull_HomePage.robot

*** Keywords ***
I will Navigate to SoliHull Webpage
    Validate SoliHull Webpage is opened
    Validate By Default Language is English
    Print the Current Page Title

I select the Language Starting with 'C'
    Click on Language Drop Down Menu
    ${Count}=   Count the number of Languages starting with Letter 'C' from Menu
    [Return]    ${Count}

I will display the title in console
    [Arguments]     ${Count}
    Select the Language starting with Letter 'C'            ${Count}