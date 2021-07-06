*** Settings ***
Library                     SeleniumLibrary
Resource                    Salesforce_LoginPage.robot
Resource                    Salesforce_HomePage.robot
Resource                    Salesforce_UserPage.robot


*** Keywords ***
I Navigate to Salesforce URL
    Validate Salesforce URL Opened

I Login into Salesforce with "${Username}" and "${Password}"
    Provide "${Username}" and "${Password}"
    Login with credential

I Navigate to Salesforce Homepage
    Validate Salesforce Homepage opened

I will try to create new user
    Click on Users option under Administration
    Validate Users page is opened
    Validate New User Creation Display
    Click on New User Button

I will fill up the user creation form
    Validate New User Form Display
    Provide all user details in Form

I submit the form and My user created successfully
    Submit the user creation form
    Validate new user created successfully
