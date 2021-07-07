*** Settings ***
Library                             SeleniumLibrary

*** Variables ***
${Logo}                             //img[@alt='Solihull Sixth Form College Logo']
${DropDown}                         //div[@class='selected']
${ListVisible}                      //div[@style='display: block;']
${TotalLaunguage}                   //div[@style='display: block;']/child::a[starts-with(text(),' C')]
${Path}                             //div[@style='display: block;']/child::a[starts-with(text(),' C')][
${Close}                            ]
${Deselect}                         //div[@class='selected']//following-sibling::div[@style='display: none;']
${DropDownClose}                    //div[@class='selected']//child::a[@class='open']

*** Keywords ***
Validate SoliHull Webpage is opened
    Page Should Contain Image       ${Logo}

Validate By Default Language is English
    Page Should Contain             English

Print the Current Page Title
    ${Title}                        Get Title
    Log to console                  ${\n}
    Log to console                  Current English Title is: ${Title}

Click on Language Drop Down Menu
    Click Element                   ${DropDown}

Count the number of Languages starting with Letter 'C' from Menu
    Wait Until Element Is Visible     ${ListVisible}
    ${Count}                        Get Element Count               ${TotalLaunguage}
    Log to Console                  ${\n}
    Log to Console                  Below are all Titles with Laguage starting with Letter 'C':
    [Return]    ${Count}

Select the Language starting with Letter 'C'
    [Arguments]     ${Count}
    ${Count}        Evaluate    ${Count}+1
    FOR     ${x}    IN RANGE    1   ${Count}
        Click Element             ${Path}${x}${Close}
        Wait Until Element Is Enabled       ${Deselect}         timeout=10
        ${NewTitle}        Get Title
        log to console      ${NewTitle}
        Wait Until Element Is Not Visible       ${DropDownClose}        timeout=10
        Click Element                     ${DropDown}
        Wait Until Element Is Visible     ${ListVisible}
    END
