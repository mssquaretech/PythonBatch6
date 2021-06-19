*** Settings ***
Library                                     SeleniumLibrary
Resource                                    ../Configuration/ENV1.robot
Resource                                    Pages/PMOHomePage.robot
Resource                                    Pages/PMOLoksabha.robot
#Resource                                   ../Configuration/ENV2.robot


*** Variables ***


*** Keywords ***
I navigate to "${URL}" on Browser
     open browser    ${URL}      ${Browser}
     maximize browser window
     Set Selenium Implicit wait  10
     capture page screenshot


I move to the bottom of page
      LoadPageStrategy
      Move to OurGov Title below in the page

I see multiple links to different pages
       Get the Links inside a List

I click on all the links
        Iterate through List of Urls

I navigate through all the pages
        Validate we are on last link

I switch back to Loksabha Page
        Switch to window Loksabha
        Validate the Loksabha Page is Loaded
I launch Profile link under the speaker
        Scroll to the botton of the page
        Click on Link "Profile"


I click on former speakers
        Click on Menu Item Former Speaker

I see the list of all former speakers
        Validate List is Visible
        Capture the list in side list element

I print Names of all former speakers
        Print Names of Speakers