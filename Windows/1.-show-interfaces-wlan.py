import os

def scan_wifi_networks():
    try:
        # Ejecutar el comando para escanear redes WiFi en Windows
        result = os.popen('netsh wlan show networks mode=B').read()

        # Mostrar la información de las redes encontradas
        print(result)

    except Exception as e:
        print(f"Error al escanear redes WiFi: {e}")

def main():
    print("Iniciando escaneo de redes WiFi...")
    
    # Escanear redes WiFi en Windows
    scan_wifi_networks()

    print("Escaneo completado.")

if __name__ == "__main__":
    main()
