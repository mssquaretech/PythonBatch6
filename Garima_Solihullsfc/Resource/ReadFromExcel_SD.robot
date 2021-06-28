*** Settings ***
Library                                     SeleniumLibrary
Resource                                    ../Configuration/EnvRFE.robot
Library                                     ../Library/CommonUtility.py
Library                                     ../Library/ReadForm.py
Library                                     OperatingSystem

*** Variables ***
${FirstName}                                fname
${LastName}                                 lname
${ListofCountry}                            country
${TextArea}                                 //textarea
${SubmitBtn}                                //a[text()='Submit']
*** Keywords ***
I Navigate to "${URL}"
        open browser        ${URL}          ${Browser}
        maximize browser window
        Set browser implicit wait       10

I Search the value fetching from Excel

        FOR     ${i}    IN RANGE     1        ${NumOfEntries}
            @{Entries}=      ReadForm.readList             ${i}          ${CURDIR}/../Data/form1.xls
#            log to console      ${Entries}[0]
             input text                     ${FirstName}        ${Entries}[0]
             input text                     ${LastName}         ${Entries}[1]
             Select From List By Label      ${ListofCountry}    ${Entries}[2]
             input text                     ${TextArea}         ${Entries}[3]
             capture page screenshot
             click Element                  ${SubmitBtn}
             Switch Window       main

        END

I Fillform and Update picking value from Excel
    ${FilledEntries}     Evaluate   ${NumOfEntries} - 1
    log to console          value updated for ${FilledEntries}  rows