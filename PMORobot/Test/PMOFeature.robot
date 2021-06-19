*** Settings ***
Documentation                This is to test PMO pages, and Print list of Speakers
Libraray                       SeleniumLibrary
Resource                     ../Resource/PMOStepDefinition.robot
Resource                     ../Configuration/ENV1.robot
#Suite Setup                  PreRequisites
#Test Teardown                CloseBrowsers

*** Variables ***

*** Keywords ***

*** Test Cases ***
Testing PMO Website to print Speakers
    Given I navigate to "${URL}" on Browser
    When I move to the bottom of page
    And I see multiple links to different pages
    And I click on all the links
#    And I navigate through all the pages
#    And I switch back to Loksabha Page
#    And I launch Profile link under the speaker
#    And I click on former speakers
#    And I see the list of all former speakers
#    Then I print Names of all former speakers

