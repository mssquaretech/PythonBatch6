*** Settings ***
Library     SeleniumLibrary
Resource    Pages/SolihullPages.robot




*** Keywords ***
Given I Navigate to url
          open browser    ${url}   chrome
          maximize browser window
          Solihull
When I Navigate to Language seletion dropdown
          user search and click on Language selection dropdown
