*** Settings ***
Documentation                   Print page title while launguage changed in Solihull
Resource                        ../Resources/Solihull_SD.robot
Resource                        ../Configuration/config.robot
Suite Setup                     Generate screenshot directory
Test Teardown                   close current browser


*** Variables ***
${Title}                    Solihull Sixth Form College: Post 16 education, A Levels and BTECs — Solihull Sixth Form College


*** Test Cases ***
Solihull Print page title assignment
    Given I navigate to "https://www.solihullsfc.ac.uk/" in "gc"
    And I validate page title               ${Title}
    When I click on top right corner dropdown
    Then I print page title of selected languages starting with letter "C"
