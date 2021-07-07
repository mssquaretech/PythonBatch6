*** Settings ***
Documentation           Test suite to login Salesforce and create user.
Suite Setup             Open Salesforce page
Resource                ../Configuration/SFDC_env.robot
Resource                ../Resources/Salesforce_StepDefination.robot

*** Test Cases ***
Login Salesforce and create user
    Given I Navigate to Salesforce URL
    When I Login into Salesforce with "${Username}" and "${Password}"
    And I Navigate to Salesforce Homepage
    And I will try to create new user
    And I will fill up the user creation form
    Then I submit the form and My user created successfully