import os
import sqlite3
import time
import random


def get_chrome_history():
    # Ruta a la base de datos del historial de Chrome (ajustar según tu sistema operativo)
    # Por ejemplo, aquí se muestra la ruta para macOS:
    # Para macOS, por ejemplo:
    history_path = os.path.expanduser('~') + "/Library/Application Support/BraveSoftware/Brave-Browser/Default/History"

    while True:
        try:
            # Intentar acceder a la base de datos
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()

            # A modo de ejemplo, obtener los últimos 5 URLs visitados (puedes ajustar la consulta según tus necesidades)
            cursor.execute("SELECT url FROM urls ORDER BY last_visit_time DESC LIMIT 5")
            urls = cursor.fetchall()

            for url in urls:
                print(url[0])

            # Cerrar la conexión
            connection.close()

            return urls  # o lo que quieras retornar
        except sqlite3.OperationalError:
            # Si no se puede acceder a la base de datos, esperar un tiempo aleatorio y volver a intentarlo
            wait_time = random.randint(10, 60)  # espera entre 10 y 60 segundos, puedes ajustar
            print(f"Error accediendo a la base de datos. Intentando nuevamente en {wait_time} segundos...")
            time.sleep(wait_time)


def main():
    get_chrome_history()


if __name__ == '__main__':
    main()
