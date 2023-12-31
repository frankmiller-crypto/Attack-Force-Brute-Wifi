import subprocess

def check_internet_connection():
    try:
        # Escoge el comando de ping según el sistema operativo
        ping_command = "ping" 

        # Realiza un ping a 8.8.8.8 y espera un máximo de 2 segundos para la respuesta
        subprocess.check_output([ping_command, "8.8.8.8"], timeout=5)

        # Si el ping es exitoso, devuelve True (conexión a Internet)
        return True
    except subprocess.CalledProcessError:
        # Si el ping falla, devuelve False (sin conexión a Internet)
        return False
    except subprocess.TimeoutExpired:
        # Si el ping excede el tiempo de espera, devuelve False (sin conexión a Internet)
        return False

if check_internet_connection():
    print("Conectado a Internet")
else:
    print("No hay conexión a Internet")
