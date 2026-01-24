import time
import json
import requests
from datetime import datetime, timezone
import sys
import platform
import subprocess
import os

# Detect OS
IS_WINDOWS = platform.system() == "Windows"

# Platform specific imports
if IS_WINDOWS:
    import ctypes
    import winsound
    from winotify import Notification, audio
    
    # Título para control de procesos (Windows)
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("PomodoroService")
    except:
        pass
else:
    # Set process title for Linux/Unix
    sys.stdout.write("\x1b]2;PomodoroService\x07")

# Cargar configuración
try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
except Exception as e:
    sys.exit(1)

WORK_DURATION = config['work_duration_minutes'] * 60
SHORT_BREAK = config['short_break_duration_minutes'] * 60
LONG_BREAK = config['long_break_duration_minutes'] * 60
CYCLES_BEFORE_LONG = config['cycles_before_long_break']

def play_alarm(type="work"):
    if IS_WINDOWS:
        if type == "work":
            winsound.Beep(750, 400)
            winsound.Beep(1000, 500)
        else:
            winsound.Beep(1000, 300)
            winsound.Beep(800, 300)
            winsound.Beep(600, 500)
    else:
        # Linux sound logic
        # Try to use standard system sounds or beep
        sound_file = "/usr/share/sounds/freedesktop/stereo/complete.oga" # Common success sound
        if type != "work":
            sound_file = "/usr/share/sounds/freedesktop/stereo/bell.oga" # Common alert sound
            
        try:
            # Try paplay (PulseAudio) first, then aplay (ALSA)
            if subprocess.call(["which", "paplay"], stdout=subprocess.DEVNULL) == 0:
                subprocess.Popen(["paplay", sound_file], stderr=subprocess.DEVNULL)
            elif subprocess.call(["which", "aplay"], stdout=subprocess.DEVNULL) == 0:
                subprocess.Popen(["aplay", sound_file], stderr=subprocess.DEVNULL)
            else:
                # Fallback to terminal beep
                print("\a")
        except:
            pass

def send_notification(title, message):
    if IS_WINDOWS:
        try:
            # On Windows we use winotify
            toast = Notification(
                app_id="Pomodoro", 
                title=title, 
                msg=message, 
                duration="short"
            )
            toast.set_audio(audio.Default, loop=False)
            toast.show()
        except:
            pass
    else:
        # Linux notification using notify-send
        try:
            subprocess.Popen(["notify-send", title, message])
        except:
            print(f"[{title}] {message}") 

def log_cycle_to_notion(cycle_number, work_min, break_min, break_type, start_time):
    try:
        url = "https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {config['notion_api_key']}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        
        # Descripción detallada (mantenemos el contexto pero no afecta la métrica numérica)
        descripcion = (
            f"📊 Resumen de la sesión:\n"
            f"• Enfoque: {work_min} min\n"
            f"• {break_type}: {break_min} min\n"
            f"• Finalizado: {datetime.now().strftime('%H:%M:%S')}"
        )
        
        data = {
            "parent": {"database_id": config['notion_database_id']},
            "properties": {
                "Nombre": {"title": [{"text": {"content": f"🍅 Ciclo #{cycle_number}"}}]},
                # SOLUCIÓN: Aquí solo enviamos work_min
                "Duracion (min)": {"number": work_min},
                "Inicio": {"date": {"start": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")}},
                "Descripción ": {"rich_text": [{"text": {"content": descripcion}}]}
            }
        }
        requests.post(url, headers=headers, json=data, timeout=10)
    except:
        pass

# --- FLUJO AUTOMÁTICO ---
cycle_count = 0
try:
    while True:
        cycle_count += 1
        start_session_time = datetime.now(timezone.utc)
        
        # 1. INICIO TRABAJO
        play_alarm("work") 
        send_notification(f"🚀 Ciclo #{cycle_count}", f"Sesión de enfoque: {config['work_duration_minutes']} min.")
        time.sleep(WORK_DURATION)
        
        # 2. CONFIGURAR DESCANSO
        is_long = cycle_count % CYCLES_BEFORE_LONG == 0
        break_type = "Descanso Largo" if is_long else "Descanso Corto"
        break_duration = LONG_BREAK if is_long else SHORT_BREAK
        break_min = config['long_break_duration_minutes'] if is_long else config['short_break_duration_minutes']
        
        # 3. INICIO DESCANSO
        play_alarm("break")
        send_notification("☕ ¡Tiempo de descanso!", f"Iniciando {break_type} ({break_min} min).")
        time.sleep(break_duration)
        
        # 4. REGISTRO EN NOTION (Solo envía minutos de trabajo a la métrica)
        log_cycle_to_notion(cycle_count, config['work_duration_minutes'], break_min, break_type, start_session_time)
        
        time.sleep(2)

except KeyboardInterrupt:
    sys.exit(0)