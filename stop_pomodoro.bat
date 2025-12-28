@echo off
cd /d "%~dp0"
echo [🛑] Buscando procesos activos...

:: Método 1: Matar por título de ventana (Intento suave)
taskkill /F /FI "WINDOWTITLE eq PomodoroService*" /T 2>nul

:: Método 2: Matar por línea de comando (Intento fuerte - El que arregla tu problema)
wmic process where "commandline like '%%pomodoro.py%%'" call terminate 2>nul

echo.
echo [OK] El Pomodoro se ha detenido completamente.
echo Ya no recibiras mas notificaciones.
pause