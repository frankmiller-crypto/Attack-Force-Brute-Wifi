import os
from itertools import permutations
import csv

def generate_permutations():
    characters = "0123456789ABCDEF"
    permutations_list = [''.join(p) for p in permutations(characters, 8)]
    return permutations_list

def save_to_csv(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow([item])

def main():
    last_two_octets_input = input("Ingresa los dos últimos octetos de la dirección MAC que deseas utilizar (por ejemplo, 89AB): ")
    last_two_octets = last_two_octets_input.upper()

    permutations_list = generate_permutations()

    key_materials = [permutation + last_two_octets for permutation in permutations_list]

    # Guardar en el archivo CSV
    csv_file = "credenciales_wifi.csv"
    save_to_csv(csv_file, key_materials)

    print("Datos guardados en el archivo 'credenciales_wifi.csv'.")

if __name__ == "__main__":
    main()
