*** Settings ***
Documentation       Test Case to fetch and validate the Page Tile on SoliHull Webpage with Different Language.
Resource            ../Configuration/ENVDetails.robot
Resource            ../Resource/SoliHull_StepDefination.robot
Suite Setup         Open the Webpage
Test Teardown       Close the Webpage

*** Test Cases ***
Validate the SoliHull Webpage Title
    Given I will Navigate to SoliHull Webpage
    ${Count}=   When I select the Language Starting with 'C'
    Then I will display the title in console        ${Count}

