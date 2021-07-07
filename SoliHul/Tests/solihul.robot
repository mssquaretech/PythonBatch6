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
    Then validating title of page
#    When we change language from top right corner dropdown
    And changing language which starts from C
#    And print the title of page as we change language
