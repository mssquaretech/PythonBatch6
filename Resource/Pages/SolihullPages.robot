*** Settings ***
Library     SeleniumLibrary
Library      String

*** Variables ***
${Dropdwon}                               //div[@class='selected']
${Listxpath}                              //div[@class='option']/a[contains(text(),'C')]

*** Keywords ***
Solihull
       page should contain     Solihull

user search and click on Language selection dropdown
       set selenium implicit wait   5s


       ${count}          get element count     ${Listxpath}


       FOR   ${i}   IN RANGE      1   ${count}
           Click Element                     ${Dropdwon}
           wait until element is visible        (//div[@class='option']/a[contains(text(),'C')])[${i}]
           click element          (//div[@class='option']/a[contains(text(),'C')])[${i}]
           wait until element is not visible       //div[@class='selected']/a[@class='open']

           ${Lang}     get title

           log to console      ${Lang}
#           click element       ${Lang}
#           wait until element is visible        (//div[@class='option']/a[contains(text(),'C')])[${i}]


#           ELSE
#           Exit for loop
       END