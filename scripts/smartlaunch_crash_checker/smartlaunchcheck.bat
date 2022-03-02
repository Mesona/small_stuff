@echo off
tasklist /FI "IMAGENAME eq client.exe" 2>NUL | find /I /N "client.exe">NUL
if %ERRORLEVEL%==1 smartlaunchcrashed.bat