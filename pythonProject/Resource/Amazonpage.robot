*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
I nav to login screen
    open browser    https://amazon.com      chrome
    capture page screenshot