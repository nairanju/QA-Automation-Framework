*** Settings ***
Library     SeleniumLibrary
Library     SSHLibrary
Library     ../CustomLibs/awsDUlibs.py
Resource    ../Keywords/awsDUKeyword.resource


#*** Variables ***


*** Test Cases ***
TEST FOR CONNECTION ESTABLISHMENT....
    ssh_connection

