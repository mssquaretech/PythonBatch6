*** Settings ***
Library         SeleniumLibrary
Resource        UOLSearchPage.robot
Library         String

*** Variables ***
${FindPropertymenu}     //a[contains(@href,'<Menu>')]
${FindPropertyItem}     //a[contains(@href,'find-your-property')]
${Filter1}         //form//div[@class='col-lg-2 col-md-4']
${Filter2}         //div[contains(text(),'Campus')]
${Pagetitle}        //h1[text()='Find Your Property']

*** Keywords ***
Click on Menu "${Value}"
    ${FindPropertymenu}=         Replace String      ${FindPropertymenu}   <Menu>      ${Value}
    click Element           ${FindPropertymenu}

Click on Menu find-your-property
    Wait Until Element Is Visible       ${FindPropertyItem}          timeout=5
    Click Element                       ${FindPropertyItem}


Switch to new Tab
    Switch Window       new
    Page Should Contain Element   ${Pagetitle}
    capture page screenshot

Select Serch from Menu
    Click on Search Menu from list




