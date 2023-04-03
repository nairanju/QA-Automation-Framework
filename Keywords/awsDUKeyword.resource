*** Settings ***
Library     SeleniumLibrary
Library     ../CustomLibs/awsDUlibs.py
Library     SSHLibrary
Library     ../utility/awsdu_util.py
#Library     ../CustomLibs/awsdu_util.py
#Library     ../utility/awsdu_util.py
#Library     awsdu_util


*** Keywords ***
ssh_connection
    ${host}     gethost
    Log to console      ${host}
    ${username}     getusername
    Log To Console       ${username}
    Login               ${username}
    Execute Command     hostname
    Close All Connections
