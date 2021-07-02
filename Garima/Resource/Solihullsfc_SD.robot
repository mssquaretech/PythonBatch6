*** Settings ***
Library                             SeleniumLibrary
Resource                            Pages/HomePage.robot
Resource                            ../Configuration/Env.robot

*** Variables ***
${languageDropdown}                   //a[@onclick='return false;']
${languageDropdownExtend}             //a[@onclick='return false;' and  @class='open']
${Clanguagelist}                      //a[contains(@onclick,'doGTranslate') and  starts-with(@title,'C')]


*** Keywords ***
I navigate to "${URL}"
    open browser                     ${URL}            ${Browser}
    maximize browser window
    capture page screenshot
    Set Selenium Implicit wait  10

I select all languages starting with Letter "${Letter}"
    Click on Language dropdown
    Check for list of language Starting with letter "${Letter}"

I print the title of the pages with language
    Iterate through "${Letter}" Language from list and print the Titles



