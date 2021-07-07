*** Settings ***
Library             SeleniumLibrary



*** Variables ***
${clickFind}                           //ul[@class='ng-star-inserted']/child::li/a[contains(text(),'Find Your Property')]
${clickSearch}                         (//ul[@class='menu']/li/a[contains(text(),'Search')])[2]
${dropdownUniversity}                   //div[@style='z-index: 10;']
${selectUniversity}                     //span[contains(text(),'RAM')]
${dropdownCampus}                       //div[@style='z-index: 9;']
${selectCampus}                         //span[contains(text(),'Main')]
${seeResults}                           //button[contains(text(),'See')]
${dropPrice}                            (//div[@class='toggle ng-star-inserted'])[4]
${selectPrice}                          //div[@class='col-md-12 d p-0 group-view d-none d-md-flex']/descendant::span[contains(text(),'Price')]
${ResultLoading}                        //button[@class='btn btn-lg btn-primary--hover loading']
${printProperty}                        //h3[@class='card-info__address mt-2 mb-2']

*** Keywords ***
I navigate to
    [Arguments]                         ${URL}           ${BROWSER}
    open browser                        ${URL}           ${BROWSER}
    maximize browser window


I click on Find Your Property option
    Click Element                       ${clickFind}

switched to new window
    Switch Window                       NEW

click on search
    Click Element                       ${clickSearch}

select options from drop down as Royal Academy and Main Campus
    Click Element                       ${dropdownUniversity}
    Wait Until Element Is Visible       ${selectUniversity}
    Click Element                       ${selectuniversity}
    Sleep                               2s
    Click Element                       ${dropdownCampus}
    Click Element                       ${selectCampus}

click on See Results
    Click Element                       ${seeResults}
    Sleep                               30s

click on Price Low to High
    Click Element                       ${dropPrice}
    Sleep                               2s
    Click Element                       ${selectPrice}

print first 5 results
    Sleep                                   50s
    Wait Until Element Is Not Visible       ${ResultLoading}
#    Click Element                          ${printProperty}
    Get Text                                ${printProperty}



