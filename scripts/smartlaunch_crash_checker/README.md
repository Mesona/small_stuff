This script was created during a time when Smartlaunch, a software we rely on, was being particularly buggy and crashing.  This crash would have no obvious or easily noticable effects, making it difficult to detect.

I created the SLLogger.VBS to launch the batch file invisibly, so that the user would not be interrupted.  I set up a windows AT command to run the SLLogger.VBS every five minutes.

The smartlaunchcheck.bat file checks to see if Smartlaunch's process is running, and if it isn't, it then launches smartlaunchcrashed.bat.

smartlaunchcrashed.bat compiles an ipconfig report into a file, and then uses the program sendemail to send an email to the specified address, including that ipconfig report.  It is not important for this script to be run invisibly, since it will only run once.
