*** Settings ***
#Declaration        This is to test roundtrip of yatra.com
Resource        ../Resources/YatraSD.robot



*** Test Cases ***
TestingYatra to book Ticket
    Given I navigate to "https://yatra.com" in webbrowser "chrome"
    When I select round trip
    And I select City of Depature and Arrival
    And I select Depature and Return dates
    And I select number of Travellers
    And I select economy class
    And I select NonStop Flights
    And I click on Search Button
    Then I see list of flights
