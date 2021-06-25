*** Settings ***
Library                     OperatingSystem
Resource                    ../Resource/Pages/Adhoc.robot
*** Variables ***
${URL}                      https://www.solihullsfc.ac.uk/
${Browser}                  chrome
${Letter}                   C


*** Keywords ***
PreRequisite
    Generate ScreenShots

closeBrowser
    close all browsers
