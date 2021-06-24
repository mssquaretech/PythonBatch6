*** Settings ***
Library                             SeleniumLibrary

*** Variables ***
${Listfight}                            //div[@class= 'result-set pr grid']/div/div


*** Keywords ***

list check
    page should contain                     Search Again
    page should contain element             ${Listfight}
    capture page screenshot