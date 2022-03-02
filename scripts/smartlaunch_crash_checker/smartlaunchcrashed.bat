@echo off
ipconfig /all > C:\Smartlaunch_Crash\report.txt
Z:\tools\sendEmail\sendEmail.exe -f SENDER_EMAIL -u MESSAGE_SUBJECT -m MESSAGE_BODY -a FILES_TO_BE_SENT -t TO@EMAIL.com -s smtp.gmail.com:587 -xu SMTP_USERNAME -xp SMTP_PASSWORD -o tls=yes

schtasks /end /TN "Smartlaunch MK2"
