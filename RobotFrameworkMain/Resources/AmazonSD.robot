*** Settings ***
Library         SeleniumLibrary


*** Keywords ***
I navigate to Amazon.com
    open browser         https://www.amazon.com     Chrome
    maximize browser window
    capture page screenshot



