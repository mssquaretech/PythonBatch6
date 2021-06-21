*** Settings ***
Resource  ../Resources/YatraSD.robot

*** Variables ***
${URL}          https://yarta.com
${chrome}       chrome

*** Test Cases ***
Testing Yatra.com
    Given navigate to Yarta.com     ${URL}      ${chrome}
    Given I navigate to "https://yatra.com" website

