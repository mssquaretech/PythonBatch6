*** Settings ***
Library                                     SeleniumLibrary
Resource                                    Pages/PMOAdhoc.robot

*** Variables ***

*** Keywords ***
Validate the Loksabha Page is Loaded

Scroll to the botton of the page

Click on Link "Profile"

Click on Menu Item Former Speaker


Validate List is Visible

Capture the list in side list element


Print Names of Speakers