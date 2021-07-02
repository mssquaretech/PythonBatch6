*** Settings ***
Documentation               This TestSuite is to test the site solihullsfc and print the page title
Resource                    ../Resource/Solihullsfc_SD.robot
Resource                    ../Configuration/Env.robot
Suite Setup                 PreRequisite
Test Teardown               closeBrowser


*** Test Cases ***
Testing solihullsf webpage to change Launguage
    Given I navigate to "${URL}"
    When I select all languages starting with Letter "${Letter}"
    Then I print the title of the pages with language

