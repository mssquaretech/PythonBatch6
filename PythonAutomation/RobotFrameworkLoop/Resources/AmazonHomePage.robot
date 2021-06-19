*** Settings ***
Library                         SeleniumLibrary

*** Variables ***
${Category}                     //select[@name='url']
${DropDownOption}               //select[@name='url']/child::option


*** Keywords ***
Click on Amazon Category Drop Down
    Click Element        ${Category}

Click on All Category from Drop Down
    ${Count}            Get Element Count           ${DropDownOption}
    FOR     ${x}        IN RANGE    1   ${Count}
        Click Element       //select[@name='url']/child::option[${x}]
    END
    [Return]    ${Count}

Print the first five category only
    [Arguments]     ${Count}
    log to console      ${\n}
    FOR     ${x}    IN RANGE    1   ${Count}
    ${Text}     Get Text    //select[@name='url']/child::option[${x}]
        Run Keyword If  ${x}<=5
        ...     log to console      ${Text}
        Exit for Loop If        ${x}>5
    END