from itertools import permutations
import csv

def generate_permutations():
    characters = "0123456789ABCDEF"
    permutations_list = [''.join(p) for p in permutations(characters, 8)]
    return permutations_list

def find_registro(data, target_key):
    for i, item in enumerate(data, start=1):
        if item == target_key:
            return i
    return None

def main():
    last_two_octets_input = input("Ingresa los dos últimos octetos de la dirección MAC que deseas utilizar (por ejemplo, 72C6): ")
    last_two_octets = last_two_octets_input.upper()

    permutations_list = generate_permutations()

    key_materials = [permutation + last_two_octets for permutation in permutations_list]

    # Mostrar las combinaciones
    print("Combinaciones generadas:")
    for item in key_materials:
        print(item)

    # Buscar el número de registro para la clave especificada
    target_key = "50A5DC4D72C6"
    registro = find_registro(key_materials, target_key)

    if registro is not None:
        print(f"\nLa clave '{target_key}' se encuentra en el número de registro: {registro}")
    else:
        print(f"\nLa clave '{target_key}' no se encuentra en las combinaciones generadas.")

if __name__ == "__main__":
    main()
