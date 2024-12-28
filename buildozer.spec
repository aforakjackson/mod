[app]
title = MyOverlayWithMinimize
package.name = overlayminimize
package.domain = org.test

# El directorio donde estén main.py y overlay_service.py
source.dir = mod

# Mínimo, lo siguiente en requirements:
requirements = python3,kivy,pyjnius,android

# Permiso para superposición
android.permissions = SYSTEM_ALERT_WINDOW

# Declaración del servicio
services = overlay_service:overlay_service.py
