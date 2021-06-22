*** Settings ***

Library                 SeleniumLibrary

*** Variables ***
${languageClick}                             //div[@id="gtranslate_wrapper"]
${Langoption}                           (//div[@class='option']/descendant::a[starts-with(text(),' C')])
${optionselected}                       //div[@class="selected"]
${OptionWait}                             //div[@class="selected"]/following-sibling::div[@style="display: none;"]
${OptionWaitvisible}                        //div[@class="selected"]/following-sibling::div[@style="display: block;"]
#//div[@class="selected"]/a[@class='open']



*** Keywords ***
Check the Title of the Page
    ${Title}                    Get Title
    log to console              Page Title is: ${Title}

Select the Language
    Click element               ${languageClick}
    sleep       2s

Print the Page Title

    ${COUNT}=            Get Element Count               ${Langoption}
    log to console          total language count: ${COUNT}
    ${COUNT}    Evaluate    ${COUNT}+1

    FOR     ${i}    IN RANGE            1        ${COUNT}
        Click element                   //div[@class='option']/descendant::a[starts-with(@title,'C')][${i}]
        Wait Until Element Is Enabled               ${OptionWait}               timeout=15
        ${Title}                          Get Title
        log to console          Title as per Languages: ${Title}
        Click element               ${languageClick}
        Wait Until Element is Visible                 ${OptionWaitvisible}              timeout=15
    END