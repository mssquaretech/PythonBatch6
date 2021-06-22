*** Settings ***
Documentation           SoliHull sites assignment
Resource                ../Resource/SolihullSD.robot
Resource                ../Config/Env.robot
Suite Setup             Pre conditions for flow
Test Teardown           Close Browser

*** Test Cases ***
Assignment on Solihull website
    Given I navigate to "https://www.solihullsfc.ac.uk/" site using "chrome" browser
    When I validate "Solihull Sixth Form College" title page
    Then I Select list of langauge with starting letter            C