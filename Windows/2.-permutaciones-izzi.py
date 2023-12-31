import os
from itertools import product
from xml.etree import ElementTree as ET

def generate_combinations(last_two_octets):
    pattern = "C85261{}{}" + last_two_octets
    characters = "0123456789ABCDEF"
    combinations = [''.join(p) for p in product(characters, repeat=2)]
    formatted_combinations = [pattern.format(c[0], c[1]) for c in combinations]
    return formatted_combinations

def create_xml(ssid, key_material):
    wlan_profile = ET.Element("WLANProfile", xmlns="http://www.microsoft.com/networking/WLAN/profile/v1")

    # ... (resto del código)

    xml_tree = ET.ElementTree(wlan_profile)
    
    # Crear el directorio 'profiles' si no existe
    os.makedirs("profiles", exist_ok=True)

    # Manejar excepciones al intentar escribir el archivo
    try:
        xml_tree.write(f"profiles\\{ssid}-{key_material}.xml")
    except Exception as e:
        print(f"Error al escribir el archivo para {ssid}-{key_material}: {e}")

def main():
    try:
        last_two_octets_input = input("Ingresa los dos últimos octetos de la dirección MAC que deseas utilizar (por ejemplo, 89AB): ")
        last_two_octets = last_two_octets_input.upper()

        combinations = generate_combinations(last_two_octets)

        for combination in combinations:
            ssid = f"IZZI-{last_two_octets}"
            key_material = combination

            create_xml(ssid, key_material)

        print("Archivos XML generados en la carpeta 'profiles'.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
