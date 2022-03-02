
:: Adds white space, for readability
echo.>> macs.txt

:: Gets computer name
hostname >> macs.txt

:: Gets the MAC Address
getmac >> macs.txt

:: Removes the hyphens, which was necessary at one point
:fart.exe --remove macs.txt -

:: Replaces - with : for grabbing macs to be put into DHCP
fart.exe macs.txt - :
