import os
import sqlite3
import time
import random
import re

def get_youtube_channels():
    # Ruta a la base de datos del historial de Brave (cambia según tu SO)
    history_path = os.path.expanduser('~') + "/Library/Application Support/BraveSoftware/Brave-Browser/Default/History"
    channels = set()

    while True:
        try:
            # Intentar acceder a la base de datos
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()

            # Obtener todas las URLs visitadas
            cursor.execute("SELECT url FROM urls WHERE url LIKE 'https://www.youtube.com/%'")
            urls = cursor.fetchall()

            # Extraer canales de las URLs
            for url in urls:
                # Buscando diferentes patrones de URLs de canales
                match_c = re.search(r'https://www\.youtube\.com/c/([^/?&]+)', url[0])
                match_channel = re.search(r'https://www\.youtube\.com/channel/([^/?&]+)', url[0])

                if match_c:
                    channels.add(match_c.group(1))
                elif match_channel:
                    channels.add(match_channel.group(1))

            connection.close()
            return channels
        except sqlite3.OperationalError:
            wait_time = random.randint(10, 60)
            print(f"Error accediendo a la base de datos. Intentando nuevamente en {wait_time} segundos...")
            time.sleep(wait_time)

def main():
    channels = get_youtube_channels()

    # Guardar los canales en un archivo en el escritorio
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop", "youtube_channels.txt")
    with open(desktop_path, 'w') as f:
        for channel in channels:
            f.write(channel + "\n")

    print(f"Canales de YouTube guardados en {desktop_path}")

if __name__ == '__main__':
    main()
