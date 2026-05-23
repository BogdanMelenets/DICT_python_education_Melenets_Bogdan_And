import requests
import json
import re
from bs4 import BeautifulSoup

# https://dummyjson.com/quotes/random (цитати працює з json)
# https://zenquotes.io                (цитати працює по txt)
# https://www.themoviedb.org/movie/1380291-tom-clancy-s-jack-ryan-ghost-war (фільм 1)
# https://www.themoviedb.org/movie/1304313-lee-cronin-s-the-mummy (фільм 1)
url = input("Input the URL:")


try:
    response = requests.get(url, timeout=5) # timeout задає час очікування у секундах

    #response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'}, timeout=5)
    response.raise_for_status() # Викидає помилку для кодів 4xx або 5xx
    print("Дані успішно отримано:")

    # print("Дані із json")
    try:
       # data = response.json()
       # print("Цитати: ", data["quote"])

        soup = BeautifulSoup(response.text, "html.parser")

        # Назва фільму з тегу <title>
        title_tag = soup.find("title")
        movie_title = (
            title_tag.text.strip() if title_tag else "Invalid quote resource!"
        )

        # Опис фільму в тегу <meta name="description">
        meta_description_tag = soup.find("meta", {"name": "description"})

        # Отримуємо доступ через ['content'], якщо тег існує
        if meta_description_tag and "content" in meta_description_tag.attrs:
            movie_description = meta_description_tag["content"].strip()
        else:
            movie_description = "Invalid quote resource!"

        # Формуємо та повертаємо підсумковий словник
        movie_data = {"Назва": movie_title, "Опис": movie_description}

        print (movie_data)
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

