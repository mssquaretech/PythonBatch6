*** Settings ***
Library                           SeleniumLibrary
Resource                          ./Page/SolihullPage.robot


*** Keywords ***

I navigate to "${Websitelink}" site using "${BrowserApp}" browser

    Open Browser                 ${Websitelink}        ${BrowserApp}
    Maximize Browser Window
    Capture Page Screenshot

I validate "${PageTitle}" title page
    Validate "${PageTitle}"

I Select list of langauge with starting letter
    [Arguments]                        ${LetterStartSearch}
    Select langauge list               ${LetterStartSearch}



