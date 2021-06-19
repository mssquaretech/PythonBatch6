*** Settings ***
Library                         SeleniumLibrary

*** Variables ***

${SearchLink}                              //aside[@id='sidebar-first']/descendant::li[contains(@class,'first leaf')]
${UniversityDropDown}                      //div[@class='container-fluid']//div[text()=' University ']
${UniversitydropdownOpened}                //div[@class='options']
${SelectUniversityName}                    //span[text()='Royal Academy of Music (RAM)']
${CampusElement}                           //div[text()=' Campus ']
${SelectCampusElement}                     //span[text()='Main Campus']
${ClickSubmit}                             //div[@class='row filter-row']/descendant::div[@class='submit-group']/button
${Resultshown}                             //p[contains(@class,'number-of-result')]
${FilteroptionClick}                       //div[contains(@class,'col-md-2 ng-touched')]/descendant::div[@class='value ng-star-inserted']
${SelectfromFilterOption}                  //span[contains(text(),'Low to High')]
${SeachLoadingXapth}                       //button[@class='btn btn-lg btn-primary--hover loading']
${NumberofLinks}                           //h3[@class='card-info__address mt-2 mb-2']


*** Keywords ***
Move to found out proprty window
    ${hanldes}=                             Get Window Handles
    switch window                           ${hanldes}[1]

Click on search
    click element                           ${SearchLink}
    page should contain                     Search A Property

Select university
     click element                          ${UniversityDropDown}
     Wait until element is visible          ${UniversitydropdownOpened}
     click element                          ${SelectUniversityName}

Select campus
     Wait until element is visible          ${CampusElement}
     click element                          ${CampusElement}
     click element                          ${SelectCampusElement}

Click Submit
     Click element                          ${ClickSubmit}

     Wait until element is visible          ${Resultshown}                          30s
     capture page screenshot

Selection of required filter
     Click element                           ${FilteroptionClick}
     Click element                           ${SelectfromFilterOption}

     Wait until element is visible          ${SelectfromFilterOption}
     Wait until element is not visible          ${SeachLoadingXapth}                    40s

Print required "${linksRequired}" of university Name
     @{NumberoflistLinkitem}=               get web elements                       ${NumberofLinks}
     ${CountLink}=                          get length                      ${NumberoflistLinkitem}

     FOR    ${i}        IN RANGE            1           ${CountLink}

            ${x}          get text           (//h3[@class='card-info__address mt-2 mb-2'])[${i}]

            run keyword If      ${i}<${linksRequired}
            ...     log to console      ${x}

            exit for loop if        ${i}==${linksRequired}


     END
