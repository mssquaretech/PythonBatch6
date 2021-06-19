*** Settings ***

Library         SeleniumLibrary
Resource         ../Config/Envi1.robot
Resource         ../Resource/HomePage/HomepageElements.robot
Resource         ../Test/HousingSearchFF.robot
Resource         ../Resource/FiindPropertyPage/FindProperty.robot

*** Keywords ***

User login to househunt webpage
    open browser            ${URL}              ${Brower}
    maximize browser window

Click on Find your property
    click element           ${FindPropertyElement}

Switch the window
    switch window            NEW

Select value from Drop Down
     wait until element is visible          ${SearchBtn}
     click element                          ${SearchBtn}
     wait until element is visible          ${TextElement}
     #select all from list               //span[contains(text(),'Royal Academy ')]
     click element                          ${DDElement}
     wait until element is visible          ${OptionElement}
     click element                          ${OptionElement}
     click element                          ${TextElement}
     click element                          ${MainCampusSSBox}
     wait until element is visible          ${MainCampusElement}
     click element                          ${MainCampusElement}
     click element                          ${SeeResultsBtn}

Sort from Low to High
     wait until element is visible      ${SortElement}                  timeout=20
     click element                      ${SortElement}
     click element                      ${LtoHElement}
     wait until page does not contain element      ${LoadingBtn}          timeout=50

Result is Displayed
      FOR       ${i}        IN RANGE        1           6
            ${HouseName}     get text              (//h3[@class='card-info__address mt-2 mb-2'])[${i}]
            log to console        ${HouseName}
      END