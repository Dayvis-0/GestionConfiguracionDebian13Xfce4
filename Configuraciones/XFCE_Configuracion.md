# Mi Configuración XFCE

Documentación detallada de todas las configuraciones personalizadas de XFCE en este setup.

## 🎨 Apariencia y Temas

### Tema GTK e Iconos
- **Tema GTK**: `Gradient-Dark-GTK`
- **Tema de Iconos**: `Papirus-Dark`
- **Panel modo oscuro**: Activado

### Panel Principal
- **Posición**: Abajo (p=8;x=960;y=1060)
- **Longitud**: 100% del ancho
- **Tamaño**: 26px
- **Iconos**: 16px
- **Posición bloqueada**: Sí
- **Borde**: 2px
- **Fondo**: Imagen personalizada (`/home/dayvis/Documentos/Fondo/1096012.jpg`)
- **Estilo de fondo**: Estilo 2 (imagen)

## ⌨️ Atajos de Teclado Personalizados

### Atajos de Aplicaciones (Super + Tecla)
- `Super + E` → **Thunar** (administrador de archivos)
- `Super + W` → **Brave Browser**
- `Super + T` → **Ghostty** (terminal)
- `Super + C` → **Visual Studio Code**
- `Super + L` → **Bloqueo de pantalla** (xflock4)
- `Super + D` → **DBeaver** (base de datos)
- `Super + I` → **Discord**
- `Super + F` → **Firefox**
- `Super + G` → **Google Chrome**
- `Super + A` → **AnyDesk**
- `Super + B` → **Brave Browser** (Google)
- `Super + V` → **CopyQ** (portapapeles)
- `Super + Bar` → **App Finder** (launcher de aplicaciones)

### Atajos de Sistema (Ctrl + Alt + Tecla)
- `Ctrl + Alt + T` → **Terminal** (exo-open)
- `Ctrl + Shift + Escape` → **Gestor de tareas** (xfce4-taskmanager)

### Atajos de Captura de Pantalla
- `Print` → **Captura de pantalla con timestamp** (área)
- `Ctrl + Print` → **Captura completa con timestamp**

### Configuración de Capturas
- **Ruta**: `/home/dayvis/Imágenes/Capturas de pantalla/`
- **Formato**: `Captura_pantalla_YYYY-MM-DD_HH-MM-SS.png`
- **Guardar al portapapeles**: Sí (-c)

## 🪟 Gestor de Ventanas (Xfwm4)

### Comportamiento de Ventanas
- **Acción al activar**: Traer al frente
- **Maximizar sin bordes**: Sí
- **Movimiento de caja**: No
- **Redimensión de caja**: No
- **Click para enfocar**: Sí
- **Enfocar ventanas nuevas**: Sí

### Botones de Ventana
- **Diseño de botones**: `O|SHMC`
  - `O` = Botón de menú de ventana
  - `|` = Separador
  - `S` = Enrollar (Shade)
  - `H` = Maximizar
  - `M` = Minimizar
  - `C` = Cerrar

### Acciones de Ventana
- **Doble click**: Maximizar
- **Distancia de doble click**: 5px
- **Tiempo de doble click**: 250ms
- **Easy Click**: Tecla Super

### Ciclado de Ventanas (Alt+Tab)
- **Dibujar marco**: Sí
- **Enfocar al ciclar**: No
- **Mostrar ocultas**: Sí
- **Mostrar minimizadas**: No
- **Vista previa**: Sí
- **Modo**: 0 (vista previa completa)

### Transparencia y Bordes
- **Opacidad del marco**: 100%
- **Borde superior**: 0px
- **Opacidad activa**: 100%
- **Opacidad inactiva**: 100%
- **Opacidad del popup**: 100%
- **Opacidad del menú**: 95%

## 📋 Panel y Plugins

### Plugins del Panel (ordenados)
1. **Menú de Aplicaciones** (applicationsmenu)
2. **Lista de Tareas** (tasklist)
   - **Agrupamiento**: 1 (por aplicación)
3. **Separador** (separator)
   - **Expandible**: Sí
   - **Estilo**: 0 (línea)
4. **[Más plugins...]** (continúa en archivo completo)

### Configuración de Separadores
- **Separador expandible**: Para espacios flexibles
- **Separadores fijos**: Para divisiones visuales

## 🔧 Otras Configuraciones

### Thunar (Administrador de Archivos)
- Configuraciones personalizadas de navegación y vista
- Atajos de teclado específicos
- Configuración de menú contextual

### Sesion y Aplicaciones al Inicio
- Aplicaciones configuradas para iniciar con el sistema
- Gestión de sesión personalizada

### Gestión de Energía
- Configuración de batería y suspensión
- Comportamiento de pantalla

### Notificaciones
- Configuración de xfce4-notifyd
- Posicionamiento y duración de notificaciones

### Configuración de Teclados
- Distribuciones de teclado configuradas
- Comportamiento de teclas especiales

### Configuración de Pantallas
- Configuración de monitores
- Resoluciones y posicionamiento

## 📁 Estructura de Archivos de Configuración

```
xfce4/
├── xfconf/xfce-perchannel-xml/
│   ├── xfce4-keyboard-shortcuts.xml  # Atajos personalizados
│   ├── xfwm4.xml                     # Gestor de ventanas
│   ├── xfce4-panel.xml               # Configuración de paneles
│   ├── xsettings.xml                 # Temas y apariencia
│   ├── thunar.xml                    # Administrador de archivos
│   ├── xfce4-desktop.xml             # Escritorio
│   ├── xfce4-session.xml             # Sesión y arranque
│   ├── xfce4-notifyd.xml             # Notificaciones
│   ├── xfce4-power-manager.xml        # Gestión de energía
│   ├── keyboards.xml                 # Configuración de teclados
│   ├── displays.xml                  # Configuración de pantallas
│   └── [demás archivos de configuración]
├── panel/
│   └── xfce4-clipman-actions.xml     # Configuración de portapapeles
└── [otras configuraciones específicas]
```

## 🚀 Instalación de esta Configuración

Para instalar esta configuración en un sistema nuevo:

1. **Copiar archivos**:
   ```bash
   cp -r xfce4/* ~/.config/xfce4/
   ```

2. **Reiniciar sesión**:
   ```bash
   # Cerrar sesión y volver a iniciar
   # o reiniciar XFCE si es posible
   ```

3. **Verificar dependencias**:
   - Asegurarse que todas las aplicaciones de atajos estén instaladas
   - Verificar que los temas (`Gradient-Dark-GTK`, `Papirus-Dark`) estén disponibles

## ⚠️ Notas Importantes

- Los atajos de teclado usan la tecla **Super** (tecla Windows)
- Las capturas de pantalla se guardan automáticamente con timestamp
- El panel tiene fondo personalizado - asegurarse que la imagen exista
- Algunas aplicaciones pueden necesitar instalación manual

## 🔄 Mantenimiento

- **Actualización**: Cuando se hagan cambios, actualizar usando el script `xfce_config_manager.py`
- **Backup**: El gestor mantiene backups automáticos de configuraciones
- **Sincronización**: Para mantener actualizado entre sistemas, usar la opción 3 del gestor

---

*Esta configuración representa un setup optimizado para productividad con atajos rápidos, tema oscuro y herramientas de desarrollo preconfiguradas.*