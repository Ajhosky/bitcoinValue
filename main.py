import threading
import requests
import time
from datetime import datetime


def get_bitcoin_price():
    while True:
        # Pobierz dane z API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()

        # Wypisz aktualną cenę Bitcoina w dolarach
        price = data['bpi']['USD']['rate']
        print(f'Aktualna cena Bitcoina: {price} USD')

        # Poczekaj sekundę przed kolejnym pobraniem danych
        time.sleep(1)


def print_date():
    while True:
        # Wypisz aktualną datę z godziną
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'Aktualna data: {current_time}')

        # Poczekaj 10 sekund przed kolejnym wyświetleniem daty
        time.sleep(10)


# Utwórz wątki dla obu zadań
thread1 = threading.Thread(target=get_bitcoin_price)
thread2 = threading.Thread(target=print_date)

# Uruchom wątki
thread1.start()
thread2.start()
