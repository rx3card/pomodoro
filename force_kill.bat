@echo off
echo [☢️] DETENIENDO TODOS LOS PROCESOS DE PYTHON...
taskkill /F /IM python.exe /T
echo.
echo [✅] Se han cerrado todos los scripts de Python.
echo Ya puedes usar el start_pomodoro.bat y stop_pomodoro.bat nuevos con normalidad.
pause