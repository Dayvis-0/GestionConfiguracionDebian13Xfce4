# XFCE Configuration Manager

Gestor de configuraciones para XFCE Desktop Environment que permite guardar, restaurar y gestionar tus configuraciones personalizadas con rotación automática de backups.

## 🎯 Características

- ✅ **Detección automática** del sistema operativo y entorno XFCE
- 💾 **Backups con rotación** máximo 2 backups automáticos
- 🔄 **Restauración** desde múltiples fuentes (current_config, backups, local)
- 📂 **Gestión** de configuraciones personalizadas y locales
- 🛡️ **Confirmaciones** en todas las operaciones críticas
- 🗂️ **Submenú de backups** para fácil selección

## 📋 Requisitos

- Sistema operativo: **Linux**
- Entorno de escritorio: **XFCE**
- Python 3 instalado

## 🚀 Uso

### Ejecución

```bash
python3 xfce_config_manager.py
```

O si le diste permisos de ejecución:

```bash
./xfce_config_manager.py
```

## 📋 Opciones del Menú

#### 1. Guardar configuración
- Guarda tu configuración XFCE actual en `current_config/xfce4/`
- Te pregunta si querés crear backup adicional en `backups/`
- Si hay 2+ backups, te pregunta si eliminar el más antiguo
- Backup con timestamp: `backup_2026-01-02_23-28-27/`

#### 2. Restaurar configuración
Te permite restaurar desde:
- **Configuración guardada** (current_config/xfce4/)
- **Configuración local** (xfce4/ - tu copia master)
- **Backups** → Te lleva a submenú con lista de backups disponibles

**Submenú de Backups:**
```
💾 Selecciona backup para restaurar:
   1. backup_2026-01-02_23-28-27 (2026-01-02 23:28)
   2. backup_2026-01-01_15-30-45 (2026-01-01 15:30)
   3. Volver al menú anterior
```

#### 3. Reemplazar xfce4 local
- Reemplaza tu carpeta `xfce4/` local con la configuración guardada
- Ideal para mantener tu "master copy" actualizada
- Pide confirmación antes de reemplazar

#### 4. Salir
- Cierra el programa con confirmación `(S/n)`
- Presionar Enter acepta salir por defecto

## 📁 Estructura de Archivos

```
.
├── xfce_config_manager.py       # Script principal
├── README.md                     # Este archivo
├── xfce4/                       # Tu configuración local (master copy)
├── backups/                      # Carpeta de backups (máx 2 automáticos)
│   ├── backup_2026-01-02_23-28-27/
│   └── backup_2026-01-01_15-30-45/
├── current_config/               # Configuración guardada para uso frecuente
│   └── xfce4/                    # Tu configuración de referencia
└── ~/.config/xfce4/              # Configuración XFCE actual (en uso)
```

## 💡 Conceptos Clave

### Tipos de Configuración

1. **XFCE Actual** (`~/.config/xfce4/`)
   - Lo que está usando XFCE AHORA MISMO

2. **Configuración Local** (`./xfce4/`)
   - Tu copia master para compartir/instalar
   - La mantenés actualizada con la opción 3

3. **Configuración Guardada** (`./current_config/xfce4/`)
   - Tu referencia principal para restauraciones
   - La que más frecuentemente usás

4. **Backups** (`./backups/backup_.../`)
   - Fotos en el tiempo para seguridad
   - Máximo 2 backups con rotación automática

### Rotación de Backups
- Solo mantiene los 2 backups más recientes
- Al crear el 3er backup, elimina automáticamente el más antiguo (con tu confirmación)
- Evita consumo excesivo de espacio

## 🛠️ Ejemplo de Flujo de Trabajo

### Escenario 1: Configurar y mantener
```bash
# 1. Ajustar XFCE a tu gusto durante varios días
# 2. Opción 1: Guardar configuración (se guarda en current_config/)
# 3. Opción 3: Reemplazar xfce4 local (actualiza tu master copy)
# 4. Repetir cuando hagas cambios que te gusten
```

### Escenario 2: Experimentar seguro
```bash
# 1. Opción 1: Guardar configuración actual (backup automático)
# 2. Hacer cambios riesgosos en XFCE
# 3. Si algo sale mal:
#    - Opción 2: Restaurar → Configuración guardada
# 4. Si querés volver a un punto anterior:
#    - Opción 2: Restaurar → Backups → Elegir backup específico
```

### Escenario 3: Instalar en sistema nuevo
```bash
# 1. Copiar tu carpeta xfce4/ al sistema nuevo
# 2. O ejecutar el script en el sistema nuevo:
#    - Mover xfce4/ a current_config/xfce4/
#    - Opción 2: Restaurar → Configuración guardada
```

## 🔧 Configuraciones Gestionadas

El script gestiona **TODAS** las configuraciones de XFCE:

- ✅ **Apariencia**: Temas, fuentes, colores, iconos
- ✅ **Atajos de teclado**: Globales y específicos de aplicaciones
- ✅ **Paneles**: Posición, plugins, comportamiento
- ✅ **Gestor de ventanas**: Comportamiento, decoraciones, atajos
- ✅ **Escritorio**: Fondos, iconos, comportamiento de archivos
- ✅ **Aplicaciones al inicio**: Programs que inician con sesión
- ✅ **Thunar**: Configuración del administrador de archivos
- ✅ **Notificaciones**: Comportamiento y apariencia
- ✅ **Gestión de energía**: Configuración de batería
- ✅ **Configuración de teclados**: Distribuciones, comportamiento
- ✅ **Monitores**: Configuración de pantallas
- ✅ **Y todo lo demás que configures en XFCE**

## ⚠️ Notas Importantes

- **Reiniciar XFCE**: Después de restaurar configuración, reinicia sesión
- **Permisos**: El script necesita acceso de lectura/escritura en `~/.config/`
- **Espacio**: Con rotación de 2 backups, el consumo es mínimo
- **Confirmaciones**: Todas las operaciones críticas requieren confirmación
- **Compatible**: Solo funciona con XFCE en sistemas Linux

## 🔒 Seguridad

- El script **NO guarda datos personales**
- Solo gestiona archivos de configuración de XFCE
- Los backups contienen preferencias, no archivos del usuario
- Sin acceso a internet, todo funciona localmente

## 📝 Licencia

MIT License - Puedes usar, modificar y distribuir este software libremente.