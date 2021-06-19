*** Settings ***

Library        SeleniumLibrary

*** Variables ***


*** Keywords ***

*** Test Cases ***

Nav to Amazon
    open browser        https://amazon.com      chrome
    maximize browser window
    capture page screenshot
