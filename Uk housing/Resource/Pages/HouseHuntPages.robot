*** Settings ***
Documentation           Suite description
Library                 SeleniumLibrary
*** Variables ***

${FindYourPropertyXpath}            //ul[@class='ng-star-inserted']/child::li[2]
${URL}                              https://housing.london.ac.uk/find-your-property
${SearchXpath}                      (//a[@href="/find-accommodation/housing-database" and text()='Search'])[1]
${Filteroption}                     (//div[@class='toggle ng-star-inserted'])[1]
${FilterValue}                      //div[@class='options']/descendant::li[14]/span
${Filteroption2}                    (//div[@class="toggle ng-star-inserted"])[3]
${FilterValue2}                     //li[@class="highlighted ng-star-inserted"]
${ButtonXpath}                      //button[@class="btn btn-lg btn-primary--hover"]
${LowToHigh}                        //span[text()="Price: Low to High"]
${DefaultFilter}                    (//div[@class="value ng-star-inserted"])[3]
${PropertiesListXpath}              //a[@class="ng-star-inserted"]
*** Keywords ***
Load
    Page should contain         London

user click on find property
    click element                   ${FindYourPropertyXpath}

user switch to New Window
     Switch Window          New

user click on Search link
    click element                   ${SearchXpath}

user click on 1st dropdown
    set browser implicit wait   3s
    click element                   ${Filteroption}

user select required option
    select from list by value       ${FilterValue}

user click on Campus dropdown
    set browser implicit wait   3s
    click element                   ${Filteroption2}

user select value from Campus dropdown
    click element                   ${FilterValue2}

user click on Search results
    click button                    ${ButtonXpath}

user gets list of properties
    Set Selenium Speed              15s

user click on default filter
    click element                   ${DefaultFilter}
user sorted price
    click element                   ${LowToHigh}

print first 5 properties
        ${count}            get element count       ${PropertiesListXpath}

        FOR ${i}    IN RANGE    1  ${count}
        ${Property} get text        //a[@class="ng-star-inserted"][${i}]
        log to console      ${Property}

     Close Browser