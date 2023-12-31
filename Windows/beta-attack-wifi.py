import os
import subprocess
import time

# Directorio donde se encuentran los archivos XML
xml_folder = "profiles"

# Iterar sobre todos los archivos XML en el directorio
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith(".xml"):
        # Obtener el nombre del archivo sin extensión (que es el SSID)
        ssid = "IZZI-048D"

        # Agregar el perfil WLAN
        subprocess.run(["netsh", "wlan", "add", "profile", "filename=" + os.path.join(xml_folder, xml_file)])

        # Conectar al SSID
        subprocess.run(["netsh", "wlan", "connect", "ssid=" + ssid, "name=" + ssid])

        # Esperar unos segundos antes de pasar al siguiente
        time.sleep(45)

        # En caso de que no se conecte, borrar el perfil y cargar uno nuevo
        subprocess.run(["netsh", "wlan", "delete", "profile", "name=" + ssid])

        # Validar que se haya borrado el perfil
        subprocess.run(["netsh", "wlan", "show", "profile"])

        # Esperar unos segundos antes de pasar al siguiente
        time.sleep(5)

        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')

print("Conexiones WiFi completadas.")
