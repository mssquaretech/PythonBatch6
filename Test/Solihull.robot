*** Settings ***
Resource    ../Resource/SolihullSD.robot

*** Variables ***
${url}              https://www.solihullsfc.ac.uk/
${Browser}          Chrome

*** Test Cases ***
Solihullsfc
     Given I Navigate to url
     When I Navigate to Language seletion dropdown
