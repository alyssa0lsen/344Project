@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="EN416326" (taskkill /f /pid 16140)
if /i "%LOCALHOST%"=="EN416326" (taskkill /f /pid 14400)

del /F cleanup-ansys-EN416326-14400.bat
