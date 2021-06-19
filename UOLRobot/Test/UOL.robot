*** Settings ***
Documentation       this is to get list of properties from househunt.london.ac.uk
Resource            ../Resource/UOLSD.robot
Resource            ../Configuration/UOL.robot



*** Test Cases ***

Test househunt.london.ac.uk to Get List of Properties
    Given I Navigate to househunt webPage         ${URL}        ${Browser}
    When I click on Find Your Property
    When I see a new page launched
    And I Search My Properties
    And UOL page Navigates to Search filter page
    And I apply search filters and click on Search       ${University}
    Then I see the list of properties
    And I Print "5" from the list
