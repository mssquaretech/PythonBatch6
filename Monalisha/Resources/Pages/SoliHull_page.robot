*** Settings ***
Documentation                         Step defination file for each Keyword of Feature file
Library                               SeleniumLibrary
Library                               String


*** Variables ***
${PageLogoXpath}                            //img[@alt = 'Solihull Sixth Form College Logo']
${DropdownXpath}                            //div[@class = 'selected']/a
${DropDownexpandXpath}                           //div[@class = 'selected']/a[@class = 'open']
${TotalLanguageXpath}                       //div[@class = 'option']/a
${SelectedLangXpath}                        //div[@class = 'option']/a[starts-with(@title,'<StartLetter>')]


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
#    Wait Until Element Is Visible       ${TotalLanguageXpath}           timeout=4
    ${SelectedLangXpath}                replace string          ${SelectedLangXpath}        <StartLetter>       ${StartLetter}
    ${SelectedLangCount}                get element count       ${SelectedLangXpath}
    log to console                      ${\n}
    log to console                      Total Language starts with ${StartLetter} is ${SelectedLangCount}
    @{SelectedlanList}=                 get web elements        ${SelectedLangXpath}
    set global variable                 ${SelectedLangXpath}
    set global variable                 ${SelectedLangCount}
    set global variable                 @{SelectedlanList}

select language and print page title
#    Wait Until Element Is Visible       ${TotalLanguageXpath}           timeout=10
    FOR     ${i}               IN RANGE    1       ${SelectedLangCount}+1
        ${item}        set variable         (${SelectedLangXpath})[${i}]
        ${language}     Get Element Attribute       ${item}         title
        click element         ${item}
        Wait Until Element Is Not Visible      ${DropDownexpandXpath}            timeout=20
        ${currentpagetitle}     get title
        log to console                      ${\n}
        log to console          Selected language is: ${language} and title is: ${currentpagetitle}
        Wait Until Element Is Not Visible      ${DropDownexpandXpath}            timeout=5
        click on right most dropdown
        Wait Until Element Is Visible         ${DropDownexpandXpath}            timeout=5
        Exit For Loop if            ${i}==${SelectedLangCount}
    END













