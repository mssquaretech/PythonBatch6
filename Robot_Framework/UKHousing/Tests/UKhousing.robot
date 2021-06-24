*** Settings ***

Documentation                   Find property in house Hunt London with Low price
Resource                        ../Configurations/Browser.robot
Resource                        ../Resources/UKhousing_SD.robot



*** Variables ***
${URL}                              https://househunt.london.ac.uk/


*** Test Cases ***
Find property in house Hunt London
    Given I navigate to             ${URL}              ${BROWSER}
    And I check for correct page open
    When I search for property
    And I switch to new tab
    And I click on search
    And I fill dropdown with values
    And I click on See result
    And I wait for result to be loaded
    And I sort properties as Low to High
    Then I print the first five proporties



