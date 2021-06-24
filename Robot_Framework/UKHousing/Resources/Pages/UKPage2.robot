*** Settings ***
Documentation                   implementation of page 2
Library                         SeleniumLibrary

*** Variables ***

${searchXpath}                              //div[@id= 'block-menu_block-2']/descendant::a[text() = 'Search']
${uniListXpath}                             //div[@class = 'options']/descendant::li/span
${uniXpath}                                 //div[@class = 'below']/descendant::div[text() = ' University ']
${campusXpath}                              //div[text() = ' Campus ']
${campusListXpath}                          //div[@class = 'options']/descendant::li/span
${seeResultXpath}                           //button[text() = 'See Results']
${buttonLoadXpath}                          //button[@class = 'btn btn-lg btn-primary--hover']
${dropDownXpath}                            //span[text() = 'Default']
${lowToHighXpath}                           //div[@class = 'options']/descendant::li/span[contains(text(), 'Low to High')]
${flatListXpath}                            //div[@class = 'row']/descendant::h3[@class = 'card-info__address mt-2 mb-2']


*** Keywords ***
search property
    Wait Until Element Is Visible               ${searchXpath}                20sec
    click element                               ${searchXpath}

select University
    click element                               ${uniXpath}

    @{uniListEle}=            get webelements           ${uniListXpath}

    FOR                 ${bucket}          IN           @{uniListEle}
        ${buckettext}       get text            ${bucket}
        run keyword if      '${buckettext}' == 'Royal Academy of Music (RAM)'     click element          ${bucket}
        Exit For Loop if    '${buckettext}' == 'Royal Academy of Music (RAM)'
    END

select campus
    click element                               ${campusXpath}
    click element                               ${campusListXpath}

see result
    click element                               ${seeResultXpath}

wait till result appear
    Wait Until Element Is Visible              ${buttonLoadXpath}               30sec

sort low to high
    Wait Until Element Is Visible              ${dropDownXpath}                 20sec
    click element                              ${dropDownXpath}
    click element                              ${lowToHighXpath}

print property
    ${flatcount}            get element count          ${flatListXpath}

    FOR             ${i}        IN RANGE        1       ${flatcount}
        ${propertyname}         get text        (${flatListXpath})[${i}]
        run keyword if          ${i} <= 5       log to console      ${propertyname}
    END


