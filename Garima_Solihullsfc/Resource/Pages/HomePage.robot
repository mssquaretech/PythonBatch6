*** Settings ***
Library                                 SeleniumLibrary
Library                                 String
Resource                                Adhoc.robot

*** Variables ***
${languageDropdown}                     //a[@onclick='return false;']
${languageDropdownExtend}               //a[@onclick='return false;' and  @class='open']
${languagelist}                         //a[contains(@onclick,'doGTranslate') and  starts-with(@title,'<Value>')]
${languageDDUpdated}                    //a[@onclick='return false;' and contains(text(),'<Language>')]


*** Keywords ***
Click on Language dropdown
    Wait until Element is visible           ${languageDropdown}     timeout=40
    LoadPageStrategy
    click element                           ${languageDropdown}
    Wait until element is visible           ${languageDropdownExtend}   timeout=10


Check for list of language Starting with letter "${Letter}"

    ${languagelist}=             Replace string         ${languagelist}         <Value>     ${Letter}
    #log to console          ${languagelist}
    Wait until element is visible                       ${languagelist}          timeout=20
    @{ListOfLanguage}=      Get WebElements             ${languagelist}
    ${Count}=            get element count              ${languagelist}

    log to console                                      ${Count}
    Set Global Variable                                 @{ListOfLanguage}


Iterate through "${Letter}" Language from list and print the Titles
      FOR               ${language}     IN              @{ListOfLanguage}

        ${CurrentLanguage}=     get Element Attribute   ${language}      title
        Click Element                                   ${language}
        log to console                                  ${CurrentLanguage}
#        ${languageDDUpdated}=       Replace string      ${languageDDUpdated}    <Language>      ${CurrentLanguage}
#        wait until element is visible       ${languageDDUpdated}        timeout=30
        ${PageTitle}=       Get Title
        log to console                                  ${PageTitle}
        #sleep   5s
        wait until element is not visible               ${languageDropdownExtend}       timeout=10
        Click Element                                   ${languageDropdown}
        wait until element is visible                   ${languageDropdownExtend}

      END
