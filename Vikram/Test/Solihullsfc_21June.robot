*** Settings ***
Documentation    Websites Validation

Resource                ../Resource/Solihullsfc_SD.robot


*** Test Cases ***
Validation of Solihullsfc
    When I navigate to solihullsfc.ac.uk
    Then I validate the Title of the Page
    Then I change the Language
    Then I Print the Title of each Page


*** Keywords ***
Provided precondition
    Setup system under test