@echo off
:: Se ubica en la carpeta del script
cd /d "%~dp0"

echo [🚀] Iniciando Pomodoro en segundo plano...

:: Llama al VBS que a su vez llama al Python del entorno virtual
start wscript.exe "run_silent.vbs"

exit