*** Settings ***
Documentation           This project contains how to search properties  on HouseHunt.com
Library                 SeleniumLibrary
Resource            ../Resource/HouseHuntStepDefination.robot


*** Test Cases ***
Searching properties on HouseHunt.com
    Given I navigate to HouseHunt.com
    And I click to Find Your Property
    And I switch to New Window
    And I click on Search on New opened window
    And I select 1st Filter
    And I select 2nd Filter
    And I click on See results
    And I  get list of properties
    And I sort properties from Low to high
    Then I print the names of first 5 properties
