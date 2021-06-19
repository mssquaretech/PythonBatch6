*** Settings ***
Library                                     SeleniumLibrary
Resource                                    Pages/PMOAdhoc.robot

*** Variables ***
${OurGovElement}                            "//span[text()='Government']"
${LinkToDiffpages}                          "//ul[@class='our-gov clearfix']//a[@target='_blank']/img"
*** Keywords ***
LoadPageStrategy
    Execute JavaScript                       window.stop()

Move to OurGov Title below in the page
    Wait Until Element Is Visible            ${OurGovElement}     timeout=30
    Scroll Element Into View                 ${OurGovElement}


Get the Links inside a List
    @{ListofPages}          Get Web Elements        ${LinkToDiffpages}
    Set Global Variable         @{ListofPages}

Iterate through List of Urls
    FOR  ${Link}    IN      @{ListofPages}
         Click Element      ${Link}
         Get Window Title
         ${Page Title}=     Get Title
         log to console     ${Page Title}
    END

#
