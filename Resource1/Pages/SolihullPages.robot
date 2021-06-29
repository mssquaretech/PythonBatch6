*** Settings ***
Library     SeleniumLibrary
Library      String

*** Variables ***
${Dropdwon}                               //div[@class='selected']
${Listxpath}                              //div[@class='option']/a
*** Keywords ***
Solihull
       page should contain     Solihull

user search and click on Language selection dropdown
       set selenium implicit wait   5s
       Click Element                     ${Dropdwon}

       ${count}          get element count     ${Listxpath}


       FOR   ${i}   IN RANGE      1   ${count}
             ${Lang}     get text       (//div[@class='option']/a)[${i}]
             ${Lang1}             Should Contain    ${Lang}     C
             Run keyword if ${Lang1} == ${Lang}
                click element    ${Lang1}
                log to console    ${Lang1}
             ELSE Continue for loop
             Run Keyword IF ${Lang1} != ${Lang}
             Exit for loop

       END