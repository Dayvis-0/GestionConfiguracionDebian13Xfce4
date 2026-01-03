#!/usr/bin/env python3
"""
XFCE Configuration Manager
Gestor de configuraciones para XFCE Desktop Environment
"""

import os
import sys
import shutil
import platform
import subprocess
from datetime import datetime
from pathlib import Path


class XFCEConfigManager:
    def __init__(self):
        self.xfce_config_path = Path.home() / ".config" / "xfce4"
        self.backup_dir = Path("backups")
        self.current_config_dir = Path("current_config")
        self.local_xfce_dir = Path("xfce4")
        
    def detect_environment(self):
        """Detecta si es Linux y XFCE"""
        os_name = platform.system()
        # Revisar múltiples variables para detectar XFCE
        desktop_session = os.environ.get('DESKTOP_SESSION', '').lower()
        xdg_desktop = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
        
        if os_name != "Linux":
            print("❌ Este script solo funciona en Linux")
            return False
            
        # XFCE se puede detectar en cualquiera de las dos variables
        if "xfce" not in desktop_session and "xfce" not in xdg_desktop:
            print("❌ No se detectó XFCE como entorno de escritorio")
            print(f"   DESKTOP_SESSION: {desktop_session}")
            print(f"   XDG_CURRENT_DESKTOP: {xdg_desktop}")
            return False
            
        print("✅ Sistema: Linux")
        print("✅ Entorno: XFCE")
        return True
    
    def verify_xfce_config(self):
        """Verifica que exista la configuración de XFCE"""
        if not self.xfce_config_path.exists():
            print(f"❌ No existe la configuración de XFCE en: {self.xfce_config_path}")
            return False
        
        print(f"✅ Configuración encontrada en: {self.xfce_config_path}")
        return True
    
    def create_directories(self):
        """Crea directorios necesarios"""
        self.backup_dir.mkdir(exist_ok=True)
        self.current_config_dir.mkdir(exist_ok=True)
    

    
    def backup_current_config_with_rotation(self):
        """Guarda configuración con rotación máximo 2 backups"""
        if not self.verify_xfce_config():
            return False
        
        print("💾 Guardando configuración...")
        
        try:
            # Obtener backups existentes y ordenarlos
            existing_backups = []
            if self.backup_dir.exists():
                existing_backups = [d for d in self.backup_dir.iterdir() if d.is_dir()]
                existing_backups.sort(key=lambda x: x.stat().st_mtime)
            
            # Si hay 2 o más backups, eliminar el más antiguo
            if len(existing_backups) >= 2:
                oldest = existing_backups[0]
                confirm = input(f"¿Eliminar backup antiguo '{oldest.name}'? (s/N): ")
                if confirm.lower() == 's':
                    shutil.rmtree(oldest)
                    print(f"🗑️  Backup eliminado: {oldest.name}")
                else:
                    print("❌ Operación cancelada")
                    return False
            
            # Crear nuevo backup con timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_name = f"backup_{timestamp}"
            backup_path = self.backup_dir / backup_name
            
            if backup_path.exists():
                shutil.rmtree(backup_path)
            
            shutil.copytree(self.xfce_config_path, backup_path)
            
            size = sum(f.stat().st_size for f in backup_path.rglob('*') if f.is_file())
            size_mb = size / (1024 * 1024)
            
            print(f"✅ Backup creado: {backup_name}")
            print(f"   Tamaño: {size_mb:.2f} MB")
            
            # Mostrar backups actuales
            current_backups = [d for d in self.backup_dir.iterdir() if d.is_dir()]
            print(f"   Backups totales: {len(current_backups)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error al crear backup: {e}")
            return False
    
    def replace_local_xfce_with_current(self):
        """Reemplaza el xfce4 local con la configuración guardada"""
        if not (self.current_config_dir / "xfce4").exists():
            print("❌ No existe configuración guardada en current_config/")
            input("Presione Enter para continuar...")
            return
        
        print("🔄 Reemplazando xfce4 local con configuración guardada...")
        
        confirm = input("¿Esto reemplazará tu carpeta xfce4/ local. Continuar? (s/N): ")
        if confirm.lower() != 's':
            print("❌ Operación cancelada")
            input("Presione Enter para continuar...")
            return
        
        try:
            # Eliminar xfce4 local
            if self.local_xfce_dir.exists():
                shutil.rmtree(self.local_xfce_dir)
            
            # Copiar configuración guardada a xfce4 local
            shutil.copytree(self.current_config_dir / "xfce4", self.local_xfce_dir)
            
            size = sum(f.stat().st_size for f in self.local_xfce_dir.rglob('*') if f.is_file())
            size_mb = size / (1024 * 1024)
            
            print("✅ xfce4 local reemplazado exitosamente")
            print(f"   Tamaño: {size_mb:.2f} MB")
            
        except Exception as e:
            print(f"❌ Error al reemplazar xfce4 local: {e}")
        
        input("Presione Enter para continuar...")
    
    def restore_from_backups(self):
        """Muestra submenú de backups para restaurar"""
        if not self.backup_dir.exists():
            print("❌ No existe la carpeta de backups")
            input("Presione Enter para continuar...")
            return
        
        backups = [d for d in self.backup_dir.iterdir() if d.is_dir()]
        backups.sort(reverse=True)  # Más recientes primero
        
        if not backups:
            print("❌ No hay backups disponibles")
            input("Presione Enter para continuar...")
            return
        
        print("\n💾 Selecciona backup para restaurar:")
        for i, backup in enumerate(backups, 1):
            backup_date = backup.stat().st_mtime
            date_str = datetime.fromtimestamp(backup_date).strftime("%Y-%m-%d %H:%M")
            print(f"   {i}. {backup.name} ({date_str})")
        
        print(f"   {len(backups) + 1}. Volver al menú anterior")
        
        try:
            choice = int(input(f"\nSelecciona opción (1-{len(backups) + 1}): "))
            
            if choice == len(backups) + 1:
                return
            
            if 1 <= choice <= len(backups):
                selected_backup = backups[choice - 1]
                confirm = input(f"¿Restaurar backup '{selected_backup.name}'? (s/N): ")
                
                if confirm.lower() == 's':
                    print("🔄 Restaurando desde backup...")
                    
                    # Eliminar configuración actual
                    if self.xfce_config_path.exists():
                        shutil.rmtree(self.xfce_config_path)
                    
                    # Copiar backup seleccionado
                    shutil.copytree(selected_backup, self.xfce_config_path)
                    
                    print("✅ Backup restaurado exitosamente")
                    print("⚠️  Reinicia tu sesión o XFCE para que los cambios se apliquen")
                else:
                    print("❌ Operación cancelada")
        
        except ValueError:
            print("❌ Opción inválida")
        
        input("Presione Enter para continuar...")
    
    def restore_config(self):
        """Restaura configuración desde current_config, backups o xfce4 local"""
        print("📁 Selecciona configuración para restaurar:")
        
        options = []
        
        # Agregar configuración guardada si existe
        if self.current_config_dir.exists() and (self.current_config_dir / "xfce4").exists():
            options.append(("Configuración guardada (current_config)", self.current_config_dir / "xfce4"))
        
        # Agregar xfce4 local si existe
        if self.local_xfce_dir.exists():
            options.append(("Configuración local (xfce4/)", self.local_xfce_dir))
        
        # Agregar opción de backups si existen
        if self.backup_dir.exists():
            backup_count = len([d for d in self.backup_dir.iterdir() if d.is_dir()])
            if backup_count > 0:
                options.append(("Backups", None))  # None para manejar specially
        
        if not options:
            print("❌ No hay configuraciones disponibles")
            input("Presione Enter para continuar...")
            return
        
        for i, (name, _) in enumerate(options, 1):
            print(f"   {i}. {name}")
        
        print(f"   {len(options) + 1}. Volver al menú principal")
        
        try:
            choice = int(input(f"\nSelecciona opción (1-{len(options) + 1}): "))
            
            if choice == len(options) + 1:
                return
            
            if 1 <= choice <= len(options):
                selected_name, config_path = options[choice - 1]
                
                # Si es backups, ir al submenú
                if selected_name == "Backups":
                    self.restore_from_backups()
                    return
                
                confirm = input(f"¿Restaurar '{selected_name}'? (s/N): ")
                if confirm.lower() == 's':
                    print("🔄 Restaurando configuración...")
                    
                    # Eliminar configuración actual
                    if self.xfce_config_path.exists():
                        shutil.rmtree(self.xfce_config_path)
                    
                    # Copiar configuración seleccionada
                    shutil.copytree(config_path, self.xfce_config_path)
                    
                    print("✅ Configuración restaurada exitosamente")
                    print("⚠️  Reinicia tu sesión o XFCE para que los cambios se apliquen")
                else:
                    print("❌ Operación cancelada")
            
        except ValueError:
            print("❌ Opción inválida")
        
        input("Presione Enter para continuar...")
    
    def save_current_config(self):
        """Guarda configuración actual con rotación de backups"""
        if not self.verify_xfce_config():
            input("Presione Enter para continuar...")
            return
        
        confirm = input("¿Guardar la configuración actual? (s/N): ")
        if confirm.lower() != 's':
            print("❌ Operación cancelada")
            input("Presione Enter para continuar...")
            return
        
        # Guardar en current_config
        try:
            # Eliminar configuración actual guardada
            if self.current_config_dir.exists():
                shutil.rmtree(self.current_config_dir)
            
            # Copiar configuración actual
            shutil.copytree(self.xfce_config_path, self.current_config_dir / "xfce4")
            
            size = sum(f.stat().st_size for f in self.current_config_dir.rglob('*') if f.is_file())
            size_mb = size / (1024 * 1024)
            
            print("✅ Configuración guardada en current_config/")
            print(f"   Tamaño: {size_mb:.2f} MB")
            
        except Exception as e:
            print(f"❌ Error al guardar configuración: {e}")
            input("Presione Enter para continuar...")
            return
        
        # Crear backup con rotación
        print()
        confirm_backup = input("¿También crear backup en backups/? (s/N): ")
        if confirm_backup.lower() == 's':
            if self.backup_current_config_with_rotation():
                print("💾 Backup creado exitosamente")
        
        input("Presione Enter para continuar...")
    
    def show_menu(self):
        """Muestra el menú principal"""
        while True:
            print("\n" + "="*50)
            print("    XFCE CONFIGURATION MANAGER")
            print("="*50)
            
            # Mostrar estado
            current_status = "✅" if self.xfce_config_path.exists() else "❌"
            print(f"Configuración XFCE actual: {current_status}")
            
            backup_count = len(list(self.backup_dir.glob("*"))) if self.backup_dir.exists() else 0
            print(f"Backups disponibles: {backup_count}")
            
            current_config_status = "✅" if (self.current_config_dir / "xfce4").exists() else "❌"
            print(f"Configuración guardada: {current_config_status}")
            
            local_xfce_status = "✅" if self.local_xfce_dir.exists() else "❌"
            print(f"Configuración local (xfce4/): {local_xfce_status}")
            
            print("\n" + "-"*30)
            print("  1. Guardar configuración")
            print("  2. Restaurar configuración")
            print("  3. Reemplazar xfce4 local")
            print("  4. Salir")
            print("-"*30)
            
            try:
                choice = int(input("\nSelecciona una opción: "))
                
                if choice == 1:
                    self.save_current_config()
                elif choice == 2:
                    self.restore_config()
                elif choice == 3:
                    self.replace_local_xfce_with_current()
                elif choice == 4:
                    confirm = input("¿Estás seguro que querés salir? (S/n): ")
                    if confirm.lower() in ['s', '']:
                        print("👋 ¡Hasta luego!")
                        break
                    else:
                        print("Continuando en el programa...")
                else:
                    print("❌ Opción inválida")
                    
            except ValueError:
                print("❌ Ingresa un número válido")
    
    def run(self):
        """Ejecuta el programa"""
        print("🔍 Detectando entorno...")
        
        if not self.detect_environment():
            input("Presione Enter para salir...")
            return
        
        if not self.verify_xfce_config():
            input("Presione Enter para salir...")
            return
        
        self.create_directories()
        self.show_menu()


if __name__ == "__main__":
    try:
        manager = XFCEConfigManager()
        manager.run()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)