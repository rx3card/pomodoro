# 🐧 Guía de Instalación y Uso en Linux

Esta guía detalla paso a paso cómo configurar y ejecutar el sistema Pomodoro en cualquier distribución Linux.

## 📋 1. Requisitos del Sistema

El script utiliza Python y algunas herramientas del sistema para notificaciones y sonidos.

### Dependencias del Sistema
Dependiendo de tui distribución, es posible que necesites instalar algunas librerías para que las notificaciones funcionen correctamente (`notify-send`) y para reproducir sonidos.

**Ubuntu / Debian / Linux Mint:**
```bash
sudo apt update
sudo apt install python3-venv libnotify-bin pulseaudio-utils vorbis-tools
```

**Fedora:**
```bash
sudo dnf install libnotify pulseaudio-utils Vorbis-tools
```

**Arch Linux / Manjaro:**
```bash
sudo pacman -S libnotify libvorbis
```

---

## 🛠️ 2. Instalación del Proyecto

### 2.1 Clonar o descargar el repositorio
Navega a la carpeta donde quieras instalar el proyecto:
```bash
cd ~/Documentos  # O tu carpeta de preferencia
# git clone <url-del-repo> pomodoro (si usas git)
cd pomodoro
```

### 2.2 Crear entorno virtual
Es recomendable usar un entorno virtual para no mezclar librerías con tu sistema:

```bash
python3 -m venv venv
```

### 2.3 Activar el entorno
```bash
source venv/bin/activate
```

### 2.4 Instalar dependencias de Python
Instala las librerías necesarias (requests):
```bash
pip install -r requirements.txt
```

---

## ⚙️ 3. Configuración

Antes de iniciar, necesitas crear el archivo de configuración.

1. Crea un archivo llamado `config.json` en la carpeta del proyecto.
2. Pega el siguiente contenido y edita tus claves de Notion:

```json
{
  "notion_api_key": "tu_secreto_de_notion",
  "notion_database_id": "id_de_tu_base_de_datos",
  "work_duration_minutes": 25,
  "short_break_duration_minutes": 5,
  "long_break_duration_minutes": 15,
  "cycles_before_long_break": 4
}
```

> **Tip:** Puedes ejecutar `python3 configurar_tiempos.py` para cambiar los tiempos cómodamente desde la terminal.

---

## 🚀 4. Ejecución

Para facilitar el uso en Linux, hemos incluido scripts `.sh` que funcionan igual que los `.bat` de Windows.

### 4.1 Dar permisos de ejecución (Solo la primera vez)
Debes decirle a Linux que estos archivos son programas ejecutables:

```bash
chmod +x start.sh stop.sh
```

### 4.2 Iniciar el Pomodoro
Para iniciar el servicio en segundo plano (liberando tu terminal):

```bash
./start.sh
```
*Verás una notificación de sistema confirmando el inicio.*

### 4.3 Detener el Pomodoro
Para detener el servicio:

```bash
./stop.sh
```

---

## 💡 Truco Pro: Crear un Alias

Si quieres ejecutar el pomodoro desde cualquier carpeta sin tener que ir a la ruta del proyecto, puedes añadir un alias a tu archivo `.bashrc` o `.zshrc`.

1. Abre tu configuración de shell:
   ```bash
   nano ~/.bashrc  # O ~/.zshrc
   ```

2. Añade estas líneas al final (ajusta la ruta a donde tengas la carpeta):
   ```bash
   alias start-pomo='/home/tu_usuario/ruta/a/pomodoro/start.sh'
   alias stop-pomo='/home/tu_usuario/ruta/a/pomodoro/stop.sh'
   ```

3. Recarga la configuración:
   ```bash
   source ~/.bashrc
   ```

Ahora puedes escribir `start-pomo` en cualquier terminal para empezar a trabajar. 🍅
