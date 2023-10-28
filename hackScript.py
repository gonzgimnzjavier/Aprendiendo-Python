import os
import time
import random

def main():
    # Obtener la ruta del escritorio del usuario
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")
    print("Ruta del escritorio:", desktop_path)

    # Esperar un tiempo aleatorio entre 1 y 3 horas con minutos incluidos
    wait_time = random.randint(3600, 10800)
    hours, remainder = divmod(wait_time, 3600)
    minutes = remainder // 60
    print(f"Esperando {hours} horas y {minutes} minutos...")
    time.sleep(wait_time)

    # Crear el archivo en el escritorio después del tiempo aleatorio
    file_path = os.path.join(desktop_path, "PARATI.txt")
    with open(file_path, "w") as a:
        a.write("PARATI")

    print(f"Archivo 'PARATI.txt' creado en {desktop_path}")

if __name__ == '__main__':
    main()
