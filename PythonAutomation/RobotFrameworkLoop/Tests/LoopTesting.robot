*** Settings ***
Resource                ../Resources/AmazonSD.robot

*** Test Cases ***
Validate Amazon Home Page
    [Tags]   E2E1
    Given I Open Amazon Home Page
    When I Select to Category
    ${Result}=  And I Click all Category
    Then I Print only Five category         ${Result}