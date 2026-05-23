import string
import requests
from bs4 import BeautifulSoup
# оскільки статті стали платними <body> відсутнє то будемо записувати в файл
# тізер статей з тегу <article__teaser>

def filename_new(title):
    translator = str.maketrans("", "", string.punctuation)
    clean_title = title.translate(translator)
    filename = clean_title.replace(" ", "_")
    return f"{filename}.txt"


def parse_nature_news():
    base_url = "https://nature.com"
    target_url = "https://nature.com/nature/articles?sort=PubDate&year=2022&page=3"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Помилка завантаження головної сторінки: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    # Знаходимо всі блоки статей на сторінці
    articles = soup.find_all("article")
    print(f"Знайдено всього статей на сторінці: {len(articles)}")

    full_saved_count = 0
    teaser_saved_count = 0

    for article in articles:
        # Шукаємо тип статті всередині тега <span> з атрибутом data-test="article.type"
        type_tag = article.find("span", {"data-test": "article.type"})
        if not type_tag:
            continue

        article_type = type_tag.get_text(strip=True)

        # Відбираємо лише статті типу "News"
        if article_type == "News":
            # Шукаємо посилання на вміст статті всередині <a> з data-track-action="view article"
            link_tag = article.find("a", {"data-track-action": "view article"})
            if not link_tag or not link_tag.get("href"):
                continue

            article_title = link_tag.get_text(strip=True)
            article_url = base_url + link_tag.get("href")

            print(f"\nОбробка статті 'News': '{article_title}'")

            # Завантажуємо внутрішню сторінку статті
            try:
                art_response = requests.get(
                    article_url, headers=headers, timeout=15
                )
                art_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Не вдалося завантажити сторінку статті: {e}")
                continue

            art_soup = BeautifulSoup(art_response.content, "html.parser")

            # 1. Спроба знайти повне тіло статті
            body_tag = art_soup.find(
                "div",
                class_=lambda c: c and any("body" in cls for cls in c.split()),
            )

            if not body_tag:
                body_tag = art_soup.find(
                    "article",
                    class_=lambda c: c and any("body" in cls for cls in c.split()),
                )

            # Формуємо універсальне ім'я файлу
            filename = filename_new(article_title)

            # Якщо тіло статті знайдено (стаття відкрита для читання)
            if body_tag:
                body_text = body_tag.get_text()

                # Зберігаємо повний вміст у бінарному режимі ('wb') з кодуванням UTF-8
                with open(filename, "wb") as file:
                    file.write(body_text.encode("utf-8"))

                print(f"-> Повний текст успішно збережено у файл: {filename}")
                full_saved_count += 1

            else:
                # 2. Якщо тіло недоступне, шукаємо хоча б короткий тизер (анонс)
                # Перевіряємо наявність класу article__teaser у тегах p або div
                teaser_tag = art_soup.find(
                    True,
                    class_=lambda c: c and any("teaser" in cls for cls in c.split()),
                )

                if teaser_tag:
                    teaser_text = teaser_tag.get_text()
                    # Додаємо помітку в текст файлу, що це лише анонс
                    prefix = "[Повний текст недоступний. Короткий тизер статті]:\n\n"
                    full_content = prefix + teaser_text

                    with open(filename, "wb") as file:
                        file.write(full_content.encode("utf-8"))

                    print(
                        f"-> Стаття закрита. Збережено лише тизер у файл: {filename}"
                    )
                    teaser_saved_count += 1
                else:
                    print(
                        f"-> Помилка: Для статті '{article_title}' не знайдено ні тіла, ні тизеру."
                    )

    # Підсумкове повідомлення про результат роботи програми
    print("\n==================================================")
    print("--- РОБОТУ ЗАВЕРШЕНО ---")
    print(f"Збережено повних текстів статей: {full_saved_count}")
    print(f"Збережено статей лише з тизером: {teaser_saved_count}")
    print(
        f"Всього створено файлів: {full_saved_count + teaser_saved_count}"
    )
    print("==================================================")


if __name__ == "__main__":
    parse_nature_news()
