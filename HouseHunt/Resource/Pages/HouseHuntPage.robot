*** Settings ***
Library                         SeleniumLibrary

*** Variables ***
${foundoutpropertyXpath}                   //nav[@class='primary-nav']/descendant::a[contains(@href,'find-your-property')]

*** Keywords ***

PageLoad
    page should contain                     Login

Click on found out property
    click element                           ${foundoutpropertyXpath}





