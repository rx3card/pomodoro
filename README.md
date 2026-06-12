# Automatizacion de la tecnica Pomodoro

Esto es un script automatizado y configurable para los ciclos de pomodoro, con la posibilidad de guardar registro en una base de datos, con **notion** (configurandolo).

## Soporte para Linux
El proyecto es compatible con Linux y Windows. 

- **Sonidos**: Intenta usar sonidos del sistema (pulseaudio/alsa). Si no están disponibles, usará el beep de la terminal.
- **Notificaciones**: Usa `notify-send` (requiere `libnotify-bin` en algunas distribuciones).
- **Scripts**: Usa `start.sh` y `stop.sh` en lugar de los `.bat`.

**[Leer Guía de Instalación en Linux](INSTALL_LINUX.md)**

## Instalación

Para poner en marcha el proyecto, sigue estos pasos:

### 1. Preparar el Entorno
Abre una terminal en la carpeta del proyecto y ejecuta los siguientes comandos:

```bash
# Crear el entorno virtual
python -m venv venv  # O: python3 -m venv venv

# Activar el entorno
.\venv\Scripts\activate      # Windows
source venv/bin/activate       # Linux

# Instalar dependencias necesarias
pip install -r requirements.txt

```

### 2. Configuración Inicial (`config.json`)

Crea un archivo llamado `config.json` en la raíz del proyecto. Este archivo contendrá tus credenciales privadas. **No lo compartas con nadie.**, esto aplica si quieres configurarlo en **notion**.
```
```json
{
  "notion_api_key": "you_secret_the_notion",
  "notion_database_id": "id_the_your_data_base",
  "work_duration_minutes": 25,
  "short_break_duration_minutes": 5,
  "long_break_duration_minutes": 15,
  "cycles_before_long_break": 4
}

```

---

## Uso y Herramientas

### Cambiar Tiempos (Configurador)

Para modificar la duración de las sesiones (Trabajo, Descanso Corto, Descanso Largo), ejecuta el script interactivo:

```bash
python configurar_tiempos.py
```

Este script actualizará automáticamente tu `config.json` con presets o valores personalizados.

### Ejecución del Pomodoro

Tienes dos opciones para iniciar el cronómetro:

1. **Windows**: Doble clic en `start_pomodoro.bat`.
2. **Linux**: Ejecuta `./start.sh` (asegúrate de dar permisos: `chmod +x start.sh`).
3. **Terminal Debug**: `python pomodoro.py`

### Detención del Sistema

Para cerrar el programa mientras corre en segundo plano, simplemente haz doble clic en:

* **Windows**: `stop_pomodoro.bat`
* **Linux**: `./stop.sh`

---

## Funcionamiento del Registro

El script está optimizado para métricas de **Deep Work**. Solo registra el ciclo una vez que el descanso ha finalizado, asegurando que la base de datos esté limpia.

| Propiedad | Tipo | Lógica de Guardado |
| --- | --- | --- |
| `Nombre` | Título | Identifica el número de ciclo (ej: Ciclo #1). |
| `Duracion (min)` | Número | **Solo guarda los minutos de trabajo** (excluye descansos). |
| `Inicio` | Fecha | Hora exactada en la que empezó la sesión de foco. |
| `Descripción ` | Texto | Resumen legible con emojis y detalles del descanso. |

---

## Alarmas y Notificaciones

El sistema utiliza sonidos diferenciados para que no tengas que mirar el reloj:

* **Pitido Agudo Doble:** Inicio de tiempo de trabajo (Enfoque).
* **Pitido Grave Triple:** Inicio de tiempo de descanso (Estiramiento).
* **Notificaciones:** Aparecen en Windows en modo `short` (desaparecen automáticamente tras unos segundos).

---

## Estructura del Proyecto

* `pomodoro.py`: Lógica principal del ciclo y conexión con API.
* `configurar_tiempos.py`: Herramienta para cambiar duraciones fácilmente.
* `start_pomodoro.bat` / `start.sh`: Lanzadores.
* `stop_pomodoro.bat` / `stop.sh`: Detenedores.
* `run_silent.vbs`: Script que permite la ejecución oculta de Python.





### 2. Archivo: `requirements.txt`
Contiene las librerías externas que Python necesita descargar.

```text
requests
winotify; sys_platform == 'win32'
```

**_Nota_**: *Debes de crear la base de datos en notion con los mismos valores-tipo que se requieren en el script. Aunque si no optas por no querer guardar tu registro en una db, simplemente omite todo el proceso de notion, el script no tendra problema con realizar las funciones sin la base de datos.*
