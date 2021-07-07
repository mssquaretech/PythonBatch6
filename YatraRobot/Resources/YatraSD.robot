*** Settings ***
Library             SeleniumLibrary


*** Keywords ***
navigate to Yarta.com
    [Arguments]         $[URL]          $[chrome]
    open browser        $[URL]          $[chrome]
    maximize browser window

I navigate to "${Link}" website
    open browser        ${Link}
    maximize browser window
