*** Settings ***
Resource                        ../Resource/ReadFromExcel_SD.robot
Documentation                   This suite is to fetch information from excel and fill online form
Library                         SeleniumLibrary
Resource                        ../Configuration/EnvRFE.robot
Suite Setup                     PreRequisite
Test Teardown                   Closure


*** Test Cases ***
Read from Excel
    Given I Navigate to "${URL}"
    When I Search the value fetching from Excel
    Then I Fillform and Update picking value from Excel

