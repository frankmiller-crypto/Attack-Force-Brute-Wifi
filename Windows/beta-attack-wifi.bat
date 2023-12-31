@echo off
setlocal enabledelayedexpansion

rem Directorio donde se encuentran los archivos XML
set "xml_folder=profiles"

rem Iterar sobre todos los archivos XML en el directorio
for %%i in ("%xml_folder%\*.xml") do (
    rem Obtener el nombre del archivo sin extensión (que es el SSID)
    set "ssid=%%~ni"
    
    rem Agregar el perfil WLAN
    netsh wlan add profile filename="%%i"
    
    rem Conectar al SSID
    netsh wlan connect ssid=IZZI-048D name=IZZI-048D

    rem Esperar unos segundos antes de pasar al siguiente
    timeout /t 60 /nobreak > nul

    rem en caso de que no se conecte borrar el perfil y cargar uno nuevo
    netsh wlan delete profile name="IZZI-048D"

    rem Validar que se haya borrado el perfil
    netsh wlan show profile
    
    rem Esperar unos segundos antes de pasar al siguiente
    timeout /t 5 /nobreak > nul

    cls
)

echo Conexiones WiFi completadas.

endlocal
