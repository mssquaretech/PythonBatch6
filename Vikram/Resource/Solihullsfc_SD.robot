*** Settings ***

Library                 SeleniumLibrary
Resource                    Pages/Solihullsfc_Homepage.robot


*** Keywords ***
I navigate to solihullsfc.ac.uk
    Open browser                https://www.solihullsfc.ac.uk/      chrome
    maximize browser window

I validate the Title of the Page
    Check the Title of the Page

I change the Language
    Select the Language

I Print the Title of each Page
    Print the Page Title

