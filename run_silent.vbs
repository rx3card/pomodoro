Set WshShell = CreateObject("WScript.Shell")
' Ejecuta python desde la carpeta venv sin mostrar ventana (el 0 significa oculto)
WshShell.Run "venv\Scripts\python.exe pomodoro.py", 0, False