import os
from itertools import permutations
import csv
from xml.etree import ElementTree as ET

def generate_permutations(last_two_octets):
    pattern = "C85261{}{}"
    characters = "0123456789ABCDEF"
    permutations_list = [''.join(p) for p in permutations(characters, 2)]
    formatted_permutations = [pattern.format(c[0], c[1] + last_two_octets) for c in permutations_list]
    return formatted_permutations

def save_to_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow([item])

def main():
    last_two_octets_input = input("Ingresa los dos últimos octetos de la dirección MAC que deseas utilizar (por ejemplo, 89AB): ")
    last_two_octets = last_two_octets_input.upper()
    
    permutations = generate_permutations(last_two_octets)

    key_materials = []
    for permutation in permutations:
        key_materials.append(permutation)

    # Guardar en el archivo CSV
    csv_file = "credenciales_wifi.csv"
    save_to_csv(csv_file, key_materials)

    print("Datos guardados en el archivo 'credenciales_wifi.csv'.")

if __name__ == "__main__":
    main()
