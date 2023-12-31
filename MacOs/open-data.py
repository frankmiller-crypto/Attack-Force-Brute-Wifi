import pandas as pd

# Ruta al archivo CSV
archivo_csv = r'C:\Users\nobody\Desktop\script-wifi-macos\script-wifi-macos\credenciales_wifi.csv'

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv(archivo_csv)

# Obtener el número total de registros (filas)
numero_total_registros = df.shape[0]
print(f'Número total de registros: {numero_total_registros}')

