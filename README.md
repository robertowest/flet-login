lo ejecutamos con python main.py

# recursos
https://flet.dev/docs/publish
https://developer.android.com/studio?hl=es-419
https://docs.flutter.dev/get-started/install/windows/desktop
https://www.oracle.com/java/technologies/downloads/
https://docs.gradle.org/current/userguide/compatibility.html


Instalación en Windows


# Publicar una app Flet en multiples plataformas
https://flet.dev/docs/publish


# Instalar Andoid Studio
Solo necesitaremos las herramientas de línea de comandos (SDK Tools)
https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip?hl=es-419


### Variables de entorno
C:\Android\SDK\cmdline-tools\bin
C:\Program Files (x86)\Android\android-sdk\cmdline-tools\7.0\bin

C:\Android\SDK\emulator
C:\Program Files (x86)\Android\android-sdk\emulator

C:\Android\SDK\platform-tools
C:\Program Files (x86)\Android\android-sdk\platforms


**Comandos en orden:**
sdkmanager --list
sdkmanager "build-tools;30.0.3"
sdkmanager "platforms;android-30"
sdkmanager "sources;android-30"
sdkmanager "system-images;android-30;default;x86_64"


# Instalar Flutter
https://storage.googleapis.com/flutter_infra_release/releases/stable/windows/flutter_windows_3.22.2-stable.zip


# Instalar Java JDK 18
https://download.oracle.com/java/22/latest/jdk-22_windows-x64_bin.msi

Verificar que la versión de java concuerde con Gradle de acuerdo al siguiente cuadro:
https://docs.gradle.org/current/userguide/compatibility.html#java


- Flet create [nombre_de_la_app]
- En assets agregar el icon.png
- Crear la app: flet build apk
- Se crea el archivo .apk en la carpeta build
