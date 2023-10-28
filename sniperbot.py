from time import sleep

from requests_html import HTMLSession

# Constantes
URL = "https://www.pccomponentes.com/asus-dual-geforce-rtx-4060-oc-edition-8gb-gddr6-dlss3"
SLEEP_INTERVAL = 30
BUY_BUTTON_SELECTOR = "#btnsWishAddBuy"


def check_buy_button(session, url):
    response = session.get(url)
    buy_zone = response.html.find(BUY_BUTTON_SELECTOR)

    if not buy_zone:
        print("No hay botón de comprar")
    else:
        # En este contexto, no tiene sentido hacer click en el botón,
        # porque estamos trabajando con una sesión HTML y no con un navegador real.
        # Simplemente informamos que el botón existe.
        print("Botón de comprar encontrado!")


def main():
    session = HTMLSession()

    while True:
        check_buy_button(session, URL)
        sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()
