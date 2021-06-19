*** Settings ***

Resource            ../Resource/YatraSD.robot
Documentation       Yahoo search flight Test case

*** Variables ***
${BROWSER}          chrome

*** Test Cases ***

Yatra flight search flow
#    Given I navigate to "https://yatra.com" home page
    Given I navigate to yatra.com home page         https://yatra.com           ${BROWSER}
    When I select road trip from delhi to mumbai
    And I select dep date as 24th June and return date 26th June
    And I select for 2 adult with economy class
    And I mark for non stop flight
    And I click on submit button
    Then I get result for only non stop flight for mention date and destination
