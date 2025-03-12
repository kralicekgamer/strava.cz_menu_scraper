@echo off
@title pip install (by OpiKula)
@chcp 65001 >nul
echo.
echo.       ██████╗ ██╗██████╗      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     
echo.       ██╔══██╗██║██╔══██╗     ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     
echo.       ██████╔╝██║██████╔╝     ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     
echo.       ██╔═══╝ ██║██╔═══╝      ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     
echo.       ██║     ██║██║          ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗
echo.       ╚═╝     ╚═╝╚═╝          ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
echo.
call :check_package requests==2.26.0
call :check_package beautifulsoup4==4.10.0
call :check_package pandas==1.3.3
call :check_package lxml==4.6.3

pause >nul
exit /b
:check_package
python -m pip show %1 >nul 2>&1
if %errorlevel% neq 0 (
    echo Balíček %1 není nainstalován, bude instalován...
    python -m pip install %1
    echo Balíček %1 byl úspěšně nainstalován.
) else (
    echo Balíček %1 je již nainstalován.
)
exit /b
pause >nul