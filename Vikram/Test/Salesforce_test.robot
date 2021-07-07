*** Settings ***
Documentation    Suite description
Library                 SeleniumLibrary
Resource                ../Resource/Salesforce_SD.robot


*** Test Cases ***
User Creation in Salesforce
    Given I navigate to Salesforce URL
    When I Enter the Credentials "${USER}" and "${PASSWRD}"
    Then I Add new user
