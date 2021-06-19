*** Settings ***
Documentation           Yatra Suite description

Resource                        ../Resource/YatraSD.robot
#Resource                       ../Resource/Pages/YatraHomepage.robot


*** Test Cases ***
Validate Yatra
        Given I navigate to Yatra.com
        When I click on Round Trip
        Then I Enter the Depart City
        And I get Some Suggestion
        Then I Click on Going To Form City
        And I Validate the Going option
        Then I Check the Depart Date
         And I Select the Depart Date
        Then I Check the Return Date
         And I Select the Return Date
        Then I Select the Non Stop Otion
        Then I Validate the Traveller Count
         And I Selct the Traveller Count
        Then I Click on Search Flight option


*** Keywords ***
Provided precondition
    Setup system under test