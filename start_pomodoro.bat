@echo off
:: Cambia el directorio de trabajos a la carpeta donde está este archivo .bat
cd /d "%~dp0"

echo [🚀] Iniciando Pomodoro en segundo plano...

:: Ejecuta el VBS usando la ruta relativa correcta
start wscript.exe "run_silent.vbs"

exit