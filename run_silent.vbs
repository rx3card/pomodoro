Set WshShell = CreateObject("WScript.Shell")
' El 0 al final significa que se ejecuta en modo oculto
WshShell.Run "venv\Scripts\python.exe pomodoro.py", 0, False