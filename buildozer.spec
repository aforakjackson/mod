[app]

# (str) Title of your application
title = PokeMMO Menu               ### <-- Nombre visible de tu app

# (str) Package name (identificador único, sin espacios)
package.name = pokemmo_menu        ### <-- Ajustado

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test          ### <-- Puedes cambiarlo, no afecta visual

# (str) Source code where the main.py lives
# Si tu main.py está en esta misma carpeta, usa "."
# Si está en carpeta "mod/", usa "mod"
source.dir = mod                     ### <-- Ajusta según tu estructura

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Separa con comas las librerías que uses además de Kivy
requirements = python3,kivy

# (list) Supported orientations (valid options: portrait, landscape, etc.)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
# 0 = False, 1 = True
fullscreen = 0

# (list) Permissions
# Ejemplo: si necesitas overlay en Android, solicita SYSTEM_ALERT_WINDOW
android.permissions = SYSTEM_ALERT_WINDOW

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# -----------------------------------------------------------------------------
# iOS / OSX / Otras configuraciones (no son cruciales para Android, 
# así que pueden quedarse como están, comentadas o con su valor por defecto)
# -----------------------------------------------------------------------------

osx.python_version = 3
osx.kivy_version = 1.9.1
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

# -----------------------------------------------------------------------------
# Python for android (p4a) specific - se dejan por defecto
# -----------------------------------------------------------------------------

#p4a.url =
#p4a.fork = kivy
#p4a.branch = master
#p4a.commit = HEAD
#p4a.source_dir =
#p4a.local_recipes =
#p4a.hook =
#p4a.bootstrap = sdl2
#p4a.port =
#p4a.setup_py = false
#p4a.extra_args =

# -----------------------------------------------------------------------------
# Buildozer
# -----------------------------------------------------------------------------

[buildozer]
log_level = 2
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

# -----------------------------------------------------------------------------
# Perfiles y otras configuraciones avanzadas (no toques si no es necesario)
# -----------------------------------------------------------------------------

#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*

#[app@demo]
#title = My Application (demo)

#[app:source.exclude_patterns@demo]
#images/hd/*

