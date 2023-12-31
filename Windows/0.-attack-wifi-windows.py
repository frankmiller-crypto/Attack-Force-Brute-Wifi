import os
import subprocess
import time
import socket
from colorama import init, Fore
from tqdm import tqdm

# Inicializar colorama
init()

# Directorio donde se encuentran los archivos XML
xml_folder = "profiles"

def check_and_exit_on_connection():
    if check_internet_connection():
        print("Conectado a Internet exitosamente. Deteniendo el script.")
        exit()

def agregar_perfil(xml_filename):
    xml_path = os.path.join(xml_folder, xml_filename)
    
    # Verificar si el archivo XML existe
    if os.path.exists(xml_path):
        subprocess.run(["netsh", "wlan", "add", "profile", "filename=" + xml_path])
        return True
    else:
        print(f"{Fore.LIGHTYELLOW_EX}Advertencia: El archivo {xml_path} no existe. No se agregará el perfil.{Fore.RESET}")
        return False

def conectar_perfil(ssid):
    # Conectar al SSID proporcionado por el usuario
    subprocess.run(["netsh", "wlan", "connect", "ssid=" + ssid, "name=" + ssid])

def agregar_perfil_y_verificar_conexion(xml_filename, user_provided_ssid):
    # Agregar el perfil y verificar la conexión
    if agregar_perfil(xml_filename):
        # Esperar unos segundos antes de conectar
        time.sleep(5)

        conectar_perfil(user_provided_ssid)

        # Esperar unos segundos antes de verificar la conexión
        time.sleep(10)

        # Verificar la conexión a Internet
        if check_internet_connection():
            print(f"{Fore.LIGHTGREEN_EX}Conectado a Internet mediante el perfil {xml_filename}. ¡Hola Vecino!{Fore.RESET}")
            exit()
        else:
            print(f"{Fore.LIGHTRED_EX}No se pudo establecer conexión a Internet mediante el perfil {xml_filename}.{Fore.RESET}")

            # Eliminar el archivo XML que no pudo establecer conexión
            os.remove(os.path.join(xml_folder, xml_filename))
            print(f"{Fore.LIGHTYELLOW_EX}Archivo {xml_filename} eliminado.{Fore.RESET}")

def check_internet_connection():
    try:
        # Intenta establecer una conexión a un servidor (por ejemplo, google.com) en el puerto 80
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

def main():
    # Obtener la lista de archivos XML en la carpeta "profiles"
    xml_files = [file for file in os.listdir(xml_folder) if file.endswith(".xml")]

    if not xml_files:
        print("No hay archivos XML en la carpeta 'profiles'.")
        return

    # Solicitar al usuario que ingrese el SSID
    user_provided_ssid = input("Ingresa el nombre del SSID al que deseas conectarte: ")

    # Iterar sobre los archivos XML existentes con una barra de progreso
    for xml_filename in tqdm(xml_files, desc="Conectando perfiles WLAN"):
        # Verificar la conexión antes de agregar el perfil y conectarse
        check_and_exit_on_connection()

        # Agregar el perfil y verificar la conexión
        agregar_perfil_y_verificar_conexion(xml_filename, user_provided_ssid)

if __name__ == "__main__":
    main()
