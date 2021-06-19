*** Settings ***
Library                                     SeleniumLibrary

*** Variables ***
${University}                               //div[text()=' University ']
${RAM}                                      //span[contains(text(),'RAM')]
${Campus}                                   //div[text()=' Campus ']
${MainCampus}                               //span[text()='Main Campus']
${Search}                                   //button[text()='See Results']
${Results}                                  //div[@class='row search-result']/child::p[text()=' results ']
${SortingButton}                            //span[text()='Default']
${Pricing}                                  //span[text()='Price: Low to High']
${AfterRefresh}                             //div[@class='submit-group']//child::button[@class='btn btn-lg btn-primary--hover']
${TotalProperty}                            //div[@class='row search-result']//child::div[@class='row']//descendant::h3
${TextXpath}                                //div[@class='row search-result']//child::div[@class='row']//descendant::h3[
${CloseXpath}                               ]

*** Keywords ***
Validate New Search Page Opened
    Page Should Contain                     Search A Property

Select 'University' and 'Campus' from Drop Down
    Click Element                           ${University}
    Wait Until Element Is Visible           ${RAM}
    Click Element                           ${RAM}
    Click Element                           ${Campus}
    Wait Until Element is Visible           ${MainCampus}
    Click Element                           ${MainCampus}

Click on Search Button
    Click Element                           ${Search}

Validate the result of properties display
    Wait Until Element Is Visible           ${Results}                  timeout=50

Click on Sorting Button
    Click Element                           ${SortingButton}

Select the Price: Low to High
    Wait Until Element Is Visible           ${Pricing}
    Click Element                           ${Pricing}

Wait till new Property List display
    Wait Until Element Is Visible           ${AfterRefresh}             timeout=50

Capture the total Properties Display and Initiate Loop to display Properties
    ${TotalCount}=                          Get Element Count           ${TotalProperty}
    Log to console                          ${\n}
    Log to console                          Top 5 Properties are:
    ${x}                                    Set Variable                1
    FOR     ${a}        IN RANGE        1       ${TotalCount}
    ${PropertyText}                     Get Text            ${TextXpath}${x}${CloseXpath}
        Run Keyword If      ${a}<=5
        ...     Run Keyword If     ${x}%2!=0
                ...     log to console      ${PropertyText}
        ${x}=       Evaluate        ${x} + 2
    Exit For Loop If        ${x}==${TotalCount}+1
    END