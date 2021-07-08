*** Settings ***
Documentation                       Salesforce Testing to create new User
Resource                            ../Resources/Salesforce_SD.robot
Resource                            ../Configurations/ENV_SF.robot

*** Test Cases ***
Salesforce User creation
    Given I navigate to             ${URL}              ${Browser}
    And I check Salesforce page is opened
    When I provide credential to login        ${UserID}       ${PWD}
    And I check Home page is opened
    Then Create unique user details
    And I try to create New user with      ${FirstName}        ${LastName}            ${EmailID}
    And I check new user created