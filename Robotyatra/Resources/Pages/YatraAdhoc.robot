*** Settings ***
Library                             SeleniumLibrary

*** Variables ***
${Expand Traveller Economy}         //i[contains(@class,'arrowpassengerBox')]
${Frame}                            //iframe[contains(@id,'container-notification-frame')]
${FrameElementclose}                //i[@class='we_forward']
${FlightsListelement}               //ul[@class='full-width no-wrap ovf-hidden']/descendant::p[contains(@class,'ellipsis')]
*** Keywords ***
Expand Traveller Economy
    click Element                   ${Expand Traveller Economy}
    sleep   1s
CloseFrame
    Select Frame                    ${Frame}
    click Element                   ${FrameElementclose}
    Unselect Frame
Print List of Flights
   @{Flights}=  Get WebElements     ${FlightsListelement}
   FOR  ${flight}  IN   @{Flights}
        log to console    ${flight}   <str>
   END
