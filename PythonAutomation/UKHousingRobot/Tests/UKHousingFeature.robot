*** Settings ***
Documentation       Robot Framework test suite to get the Housing Property at University of London
Resource            ../Resources/UKHousing_StepDefination.robot


*** Test Cases ***
Book Housing Property at University of London
    Given I Open the Housing Property Website of 'University of London'
    When I Navigate and open the 'Find Your Property' section
    And I Open the 'Search' section
    And I Select the 'University' and 'Campus'
    And I Search the Property
    And I Sort the property pricing with 'Low to High'
    Then I Capture and print the names of first 5 Properties