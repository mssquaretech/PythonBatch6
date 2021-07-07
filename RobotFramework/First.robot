*** Settings ***
Library     SeleniumLibrary
*** Variables ***

*** Keywords ***

*** Test Cases ***
Navigate to Amazon.com
    open browser    https://amazon.com      chrome
    maximize browser window
    capture page screeshot
