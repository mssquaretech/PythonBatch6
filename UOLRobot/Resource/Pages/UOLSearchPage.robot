*** Settings ***
Library         SeleniumLibrary


*** Variables ***
${SearchTab}                    (//ul[@class='menu']/li[1]/a[text()='Search'])[2]
${UniversityDropdown}           //form//div[@class='col-lg-2 col-md-4']
${CampusDropdown}               //div[contains(text(),'Campus')]
${ListUniversityDD}             //input[@autocomplete='off']
${RequiredUni}                  //span[contains(text(),'Royal Academy of Music (RAM)')]
${MainCampus}                   //span[contains(text(),'Main Campus')]
${BtnSeeResults}                //button[contains(text(),'See Results')]
${Numofresult}                  //strong[@class='number-of-result__number']
${FilterOption}                 //span[text()='Default']
${OptnLowtoHigh}                //span[text()='Price: Low to High']
${stableSearchbtn}              //button[@class='btn btn-lg btn-primary--hover']
${ListPropertyXpath}            //h3[@class='card-info__address mt-2 mb-2']

*** Keywords ***
Click on Search Menu from list
    Wait Until Element Is Visible       ${SearchTab}             timeout=5
    Click Element                       ${SearchTab}
    Wait Until Element Is Visible       ${UniversityDropdown}    timeout=5

Page contains filters
    Page Should Contain Element         ${UniversityDropdown}
    Page Should Contain Element         ${CampusDropdown}

Select filters "${University}"
    Click Element                       ${UniversityDropdown}
    Wait Until Element Is Visible       ${ListUniversityDD}
    Input Text                          ${ListUniversityDD}     ${University}
    Wait Until Element Is Visible       ${RequiredUni}
    Click Element                       ${RequiredUni}
    Click Element                       ${CampusDropdown}
    Click Element                       ${MainCampus}

Click on search
    Click Element                       ${BtnSeeResults}
    Wait Until Element Is Visible       ${Numofresult}            timeout=40

List of properties returned
    Click Element                       ${FilterOption}
    Click Element                       ${OptnLowtoHigh}
    Wait Until Element Is Visible       ${stableSearchbtn}        timeout=40
    Capture page Screenshot

print list "${Number}" of Properties

    @{ListOfproperties}=                Get Web Elements        ${ListPropertyXpath}

    ${count}    Get Element count       ${ListPropertyXpath}
    log to console      ${count}
    ${i}=   set Variable    1

    FOR     ${Property}     IN     @{ListOfproperties}
        Exit for loop If    ${i}>${Number}
            ${Title}        Get Text    ${Property}
            log to console      ${Title}
            ${i}=       Evaluate    ${i} + 1


    END

    FOR     ${X}    IN RANGE    1   ${Number}

        ${Title}            Get Text           (${ListPropertyXpath})[${X}]
        log to console      ${Title}

     END


#PrintTitle
#     [Arguments]    ${Property}
#     ${Title}        Get Text    ${Property}
#     log to console      ${Title}
#     ${i}=       Evaluate    ${i} + 1