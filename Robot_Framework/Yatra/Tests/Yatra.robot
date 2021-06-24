*** Settings ***
Resource                        ../Resources/Yatra_SD.robot
Documentation           TestSuite for Ytara flight booking

*** Variables ***
${URL}                  https://www.yatra.com/
${BROWSER}              chrome

*** Test Cases ***

Yatra Flight Booking
#    Given I navigate to "https://www.yatra.com/" in "chrome"
    Given I navigate to URL         ${URL}              ${BROWSER}
    And I check Yatra page is opened
    When I search for Round trip flight
    And I select flight from Delhi to Mumbai
    And I select departure and return date
    And I select 2 Adults of Economy class
    And I select non-stop flight
    Then I search to get the flight list
    And I check the Flight list
