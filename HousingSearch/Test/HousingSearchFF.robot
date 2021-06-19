*** Settings ***
Library                     SeleniumLibrary
Resource                    ../Resource/PropertySearchSD.robot

*** Test Cases ***

Automation to Search a Propoerty
        Given User login to househunt webpage
        When Click on Find your property
        And Switch the window
        And Select value from Drop Down
        And Sort from Low to High
        Then Result is Displayed


