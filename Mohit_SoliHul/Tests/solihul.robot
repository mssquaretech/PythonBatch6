*** Settings ***
Resource                ../Resources/solihulSD.robot
Suite Setup             Pre conditions for flow
Resource                ../Configuration/Env.robot

*** Variables ***
${url}                  https://www.solihullsfc.ac.uk/
${browser}              chrome

*** Test Cases ***
Print title of each page
    Given I navigate to                     ${url}              ${browser}
    When validating title of page
    Then changing language which starts from C

