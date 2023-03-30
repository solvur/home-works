from pprint import pprint
from bs4 import BeautifulSoup
import requests

URL = "https://rezka.ag/animation/?utm_source=canva&utm_medium=iframely"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response

def get_data_from_hdrezka(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all(
        'div', class_="b-content__inline_item"
    )
    animes = []
    for card in cards:
        info = card.find('div', calss_="b-content__inline_item-link").find('div').getText().split(", ")
        anime = {
            "title": card.find('div', class_="b-content__inline_item-link").find('a').getText(),
            "link": card.find('div', class_="b-content__inline_item-link").find('a').get("href"),
            "year": info[0],
            "country": info[1],
            "genre": info[2]
        }
        animes.append(anime)
    return animes

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animes = []
        for i in range(1, 3):
            html = get_html(f"{URL}page/1/")
            current_page = get_data_from_hdrezka(html.text)
            animes.extend(current_page)
    else:
        raise Exception("Error in parser")
