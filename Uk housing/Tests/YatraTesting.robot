*** Settings ***
Documentation           This project contains how to search flights on Yatra.com
Resource                ..//Resource/YatraStepDefination.robot


*** Test Cases ***

Searching Flights on Yatra.com
    Given I navigate to Yatra.com website
    When I select Round trip flights from Delhi to Mumbai
    And I select Departure Date and return Date
    And I select number on Adults
    And I Mark checkbox  for Non-Stop flights
    Then I will get list of flights






