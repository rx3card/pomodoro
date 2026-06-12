import json

print("CONFIGURADOR DE TIEMPOS POMODORO\n")
print("="*60)

# Cargar config actual
with open('config.json', 'r') as f:
    config = json.load(f)

print("\nConfiguración actual:")
print(f"Trabajo: {config['work_duration_minutes']} min")
print(f"Break corto: {config['short_break_duration_minutes']} min")
print(f"Break largo: {config['long_break_duration_minutes']} min")
print(f"Ciclos antes de break largo: {config['cycles_before_long_break']}\n")

print("="*60)
print("\nPRESETS DISPONIBLES:\n")
print("1. POMODORO CLÁSICO (recomendado)")
print("   Trabajo: 25 min | Break corto: 5 min | Break largo: 15 min")
print("\n2. POMODORO RÁPIDO")
print("   Trabajo: 15 min | Break corto: 3 min | Break largo: 10 min")
print("\n3. POMODORO INTENSO")
print("   Trabajo: 50 min | Break corto: 10 min | Break largo: 30 min")
print("\n4. MODO TEST (actual)")
print("   Trabajo: 0.1 min | Break corto: 0.2 min | Break largo: 0.3 min")
print("\n5. PERSONALIZADO")
print("   Tú defines los tiempos\n")

choice = input("Selecciona una opción (1-5): ").strip()

if choice == "1":
    config['work_duration_minutes'] = 25
    config['short_break_duration_minutes'] = 5
    config['long_break_duration_minutes'] = 15
    config['cycles_before_long_break'] = 4
    print("\nConfigurado: POMODORO CLÁSICO")
    
elif choice == "2":
    config['work_duration_minutes'] = 15
    config['short_break_duration_minutes'] = 3
    config['long_break_duration_minutes'] = 10
    config['cycles_before_long_break'] = 4
    print("\nConfigurado: POMODORO RÁPIDO")
    
elif choice == "3":
    config['work_duration_minutes'] = 50
    config['short_break_duration_minutes'] = 10
    config['long_break_duration_minutes'] = 30
    config['cycles_before_long_break'] = 2
    print("\nConfigurado: POMODORO INTENSO")
    
elif choice == "4":
    config['work_duration_minutes'] = 0.1
    config['short_break_duration_minutes'] = 0.2
    config['long_break_duration_minutes'] = 0.3
    config['cycles_before_long_break'] = 4
    print("\n Configurado: MODO TEST")
    
elif choice == "5":
    print("\n Ingresa los tiempos personalizados:")
    config['work_duration_minutes'] = float(input("   Trabajo (minutos): "))
    config['short_break_duration_minutes'] = float(input("   Break corto (minutos): "))
    config['long_break_duration_minutes'] = float(input("   Break largo (minutos): "))
    config['cycles_before_long_break'] = int(input("   Ciclos antes de break largo: "))
    print("\n Configurado: PERSONALIZADO")
    
else:
    print("\n Opción inválida. No se hicieron cambios.")
    exit(1)

# Guardar cambios
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print("\nNueva configuración:")
print(f"Trabajo: {config['work_duration_minutes']} min")
print(f"Break corto: {config['short_break_duration_minutes']} min")
print(f"Break largo: {config['long_break_duration_minutes']} min")
print(f"Ciclos antes de break largo: {config['cycles_before_long_break']}")
print("\nGuardado en config.json")
print("\nEjecuta: python pomodoro.py\n")