*** Settings ***
Documentation    Suite description
Library                 SeleniumLibrary


*** Variables ***
${Username}                      //input[@id="username"]
${Password}                      //input[@id="password"]
${Login}                         //input[@id="Login"]
#${VerifCode}                     //input[@id="smc"]
#${AuthVerify}                   //input[@id="save"]
${Settingicon}                  //div[@id="66:243;a"]
${UserOption}                   //li[@data-node-id="Users"]/div[@title="Users"]/button[@title="Expand"]
${CreateUser}                   (//a[contains(text(),"Users")])[2]
${NewuserFrame}                  //iframe[contains(@title, " ~ Salesforce")]
${NewUser}                       //input[@value="New User"]
${UserFrame}                      //div[@class="content iframe-parent"]/iframe[contains(@title, " ~ Salesforce")]
${userName}                         //input[@id="Username"]
${Save}                             //input[@value=" Save "]



*** Keywords ***
Enter the Credentials "${USER}" and "${PASSWRD}"
    input text              ${Username}                 ${USER}
    input text              ${Password}                 ${PASSWRD}
    Click element           ${Login}
#    Click element           ${AuthVerify}
    ${Title}                    Get Title
    log to console              Page Title is: ${Title}
    Wait Until Element is Visible                 ${UserOption}               timeout=15


Add New user
    Click element           ${UserOption}
    Click element           ${CreateUser}
    Wait Until Element is Visible                 ${NewuserFrame}                 timeout=15
    Select Frame            ${NewuserFrame}
    Click element           ${NewUser}
    Unselect Frame
    Wait Until Element is Visible                 ${UserFrame}                 timeout=15

    Select Frame             ${UserFrame}
    input text              name_firstName                  Marks1
    input text              name_lastName                   Marks1
    input text              Email                           Marks1@yopmail.com
    Click element           ${Save}






