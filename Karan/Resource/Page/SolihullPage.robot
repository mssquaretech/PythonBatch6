*** Settings ***
Library                             SeleniumLibrary
Library                             String

*** Variables ***

${SelectLanguageElement}            //div[@class='selected']/a
${DropdownOpen}                     //div[@class='selected']/a[@class='open']

*** Keywords ***
Validate "${PageTitle}"
    ${GetTitle}                         Get Title
    Should Contain                      ${GetTitle}                     ${PageTitle}

Select langauge list
     [Arguments]                        ${LetterStartSearch}
     @{ListofLanguage}=                 get webelements                 //a[starts-with(text(),' ${LetterStartSearch}')]
     ${Length}=                         get length                      ${ListofLanguage}
     log to console                     ${Length}
     ${Title}=                          Set Variable                    //title[contains(text(),'Solihull')]
     FOR           ${i}        IN RANGE         1               ${Length}+1
            Click Element                                ${SelectLanguageElement}
            Wait until element is Enabled                ${DropdownOpen}                            timeout=10
            Click Element                                //a[starts-with(text(),' ${LetterStartSearch}')][${i}]
            Wait until element is not Visible            ${DropdownOpen}                            timeout=10
            ${language}=                                 Get text                             ${SelectLanguageElement}
            ${Titletext}=                                Get Title
            log to console                               Selected Language:${language} , Title:${Titletext}
            Exit for loop if                             ${i}==${Length}

     END