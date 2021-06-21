*** Settings ***
Resource                ../Resources/UKhouseSD.robot

*** Variables ***
${URL}               https://househunt.london.ac.uk/
${BROWSER}           chrome

*** Test Cases ***
Printing top 5 results
    Given I navigate to             ${URL}           ${BROWSER}
    When I click on Find Your Property option
    And switched to new window
    And click on search
    And select options from drop down as Royal Academy and Main Campus
    And click on See Results
    And click on Price Low to High
    Then print first 5 results

