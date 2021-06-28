*** Settings ***
Documentation                         Step defination file for each Keyword of Feature file
Library                               SeleniumLibrary
Library                               String


*** Variables ***
${PageLogoXpath}                            //img[@alt = 'Solihull Sixth Form College Logo']
${DropdownXpath}                            //div[@class = 'selected']/a
#${DropDownexpandXpath}                      //div[@class = 'selected']/a[@class = 'open']
${TotalLanguageXpath}                       //div[@class = 'option']/a
${SelectedLangXpath}                        //div[@class = 'option']/a[starts-with(@title,'<StartLetter>')]
${CloseDropdownXpath}                       //div[@class='option' and @style='display: none;']
${OpenDropdownXpath}                        //div[@class='option' and @style='display: block;']


*** Keywords ***
Validate "${HomePageTitle}" is opened
    ${PageTitle}                        get title
    log to console                      ${\n}
    log to console                      Home Page title is: ${PageTitle}
    run keyword if          '${PageTitle}' == '${HomePageTitle}'         log to console          Correct Page is opened

Validate page Logo
    Page Should Contain Element         ${PageLogoXpath}

click on right most dropdown
    click element                       ${DropdownXpath}

count language starts with "${StartLetter}"
#    Wait Until Element Is Visible       ${TotalLanguageXpath}           4sec
    ${SelectedLangXpath}                replace string          ${SelectedLangXpath}        <StartLetter>       ${StartLetter}
    ${SelectedLangCount}                get element count       ${SelectedLangXpath}
    log to console                      ${\n}
    log to console                      Total Language starts with ${StartLetter} is ${SelectedLangCount}
#    @{SelectedlanList}=                 get web elements        ${SelectedLangXpath}
    set global variable                 ${SelectedLangXpath}
    set global variable                 ${SelectedLangCount}
#    set global variable                 @{SelectedlanList}

select language and print page title
#    Wait Until Element Is Visible       ${TotalLanguageXpath}           10sec
    FOR     ${i}               IN RANGE    1       ${SelectedLangCount}+1
        ${item}        set variable         (${SelectedLangXpath})[${i}]
        ${language}     Get Element Attribute       ${item}         title
        click element         ${item}
#        Wait Until Element Is Not Visible      ${DropDownexpandXpath}            20sec
        Wait Until Page Contains Element        ${CloseDropdownXpath}         10sec
        ${currentpagetitle}     get title
        log to console                      ${\n}
        log to console          Selected language is: ${language} and title is: ${currentpagetitle}
#        Wait Until Element Is Not Visible      ${DropDownexpandXpath}            5sec
        click on right most dropdown
#        Wait Until Element Is Visible         ${DropDownexpandXpath}            5sec
        Wait Until Page Contains Element        ${OpenDropdownXpath}          10sec
#        Exit For Loop if            ${i}==${SelectedLangCount}
    END
