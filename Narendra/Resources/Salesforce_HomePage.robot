*** Settings ***
Library                             SeleniumLibrary

*** Variables ***
${HomepageURL}                      https://d5g000005kxhheaw-dev-ed.lightning.force.com/lightning/setup/SetupOneHome/home
${Usersbutton}                      //div[@title='Users']//descendant::a[text()='Users']
${Userssection}                     //div[@class='bLeft']//descendant::span[text()='Users']
${UserOption}                       //ul[@role='group']//div[@title='Users']//descendant::a
${Scroll}                           //div[@title='Data']
${Userssection}                     //div[@class='bLeft']//descendant::span[text()='Users']

*** Keywords ***
Validate Salesforce Homepage opened
    ${CurrentURL}       Get Location
    Run Keyword If  '${CurrentURL}' == '${HomepageURL}'
    ...     Log to console      Correct Salesforce Homepage opened.
    ...     ELSE    Fail    Incorrect Salesforce Homepage url opened.

Click on Users option under Administration
    click element                       ${Usersbutton}
    scroll element into view            ${Scroll}
    click element                       ${UserOption}
    wait until element is visible       ${Userssection}         timeout=20s