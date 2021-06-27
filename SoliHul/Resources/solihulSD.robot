*** Settings ***
Library                                 SeleniumLibrary


*** Variables ***
${dropdown}                             //div[@class='selected']/a
${changelang}                           //a[starts-with(@Title,'C') and @href='#']
${classOpen}                            //div[@class='selected']/a[@class='open']

*** Keywords ***
I navigate to
    [Arguments]                         ${url}                  ${browser}
    open browser                        ${url}                  ${browser}
    maximize browser window

validating title of page
    Get title

#we change language from top right corner dropdown
#    Click Element                       ${dropdown}

changing language which starts from C

    @{CountryList}=         get webelements             ${changelang}


    FOR         ${selLang}          IN              @{CountryList}

                Click Element                                    ${dropdown}
                Wait until element is Enabled                    ${selLang}                 timeout=5
                Click Element                                    ${selLang}
                Wait until element is not visible                ${classOpen}               timeout=5
                ${Lang}=                    Get Element Attribute       ${selLang}             title
                ${Language}=                Get Title
                Log to console                                    Language:${Lang} , Title:${Language}
    END

#print the title of page as we change language