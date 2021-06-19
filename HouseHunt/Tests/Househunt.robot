*** Settings ***
Documentation           Househunt search script using robot framework
Resource                ../Config/Env.robot
Resource                ../Resource/HousehuntSD.robot
Resource         ../Resource/HousehuntSD.robot
Documentation       House hunt page univerity search
Resource            ../HouseHunt/HousehuntSD.robot
Resource            ../Config/Env.robot
Suite Setup         Getting screenshot under dict
Test Teardown       close browser

*** Variables ***

*** Test Cases ***

Househunt search flow
    Given I navigate to "https://househunt.london.ac.uk/" using "${BROWSER}"
    And I click on found out property link on Home Page
    And I click on search section on new window
    When I select university and campus for search
    Then I get result for selected university campus
    And I select for low to high price filter
    And I print first "8" university
