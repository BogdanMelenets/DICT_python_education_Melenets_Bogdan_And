from http.client import responses
from urllib.request import urlopen
import requests
import json
import re
#
# https://dummyjson.com/quotes/random
# https://zenquotes.io
url = input("Input the URL:")


try:
    response = requests.get(url, timeout=5) # timeout задає час очікування у секундах
    response.raise_for_status() # Викидає помилку для кодів 4xx або 5xx
    print("Дані успішно отримано:")
    print("Дані із json")
    try:
        data = response.json()
        print(data["quote"])
    except requests.exceptions.JSONDecodeError:
         if response.status_code == 200:
           print("Response was not JSON")
           # виводимо усе, що знаходиться у тегах <quote>
           print("Дані із text")
           result = re.findall(r'quote>(.*?)<',response.text)
           print(result)
except requests.exceptions.Timeout:
    print("Помилка: Час очікування підключення вичерпано (Timeout).")
except requests.exceptions.ConnectionError:
    print("Помилка: Не вдалося підключитися до сервера (перевірте інтернет).")
except requests.exceptions.HTTPError as err:
    print(f"Помилка HTTP: {err}")

