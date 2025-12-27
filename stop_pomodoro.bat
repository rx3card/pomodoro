@echo off
echo [🛑] Deteniendo Pomodoro...
taskkill /F /FI "WINDOWTITLE eq PomodoroService*" /T 2>nul
if %errorlevel%==0 (
    echo [OK] Sesion finalizada.
) else (
    echo [!] No hay sesiones activas.
)
pause