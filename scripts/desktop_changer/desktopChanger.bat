@echo off

:: Copies the Wallpapers folder from the usb to the local computer
xcopy /S /R /Y "E:\Wallpaper" "C:\Wallpaper"
 
REG ADD "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "C:\Wallpaper\Ravenclaw.jpeg" /f 
C:\Windows\System32\RUNDLL32.EXE user32.dll

shutdown -s -t 01