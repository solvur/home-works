import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/controller/"
KEY = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,"
             "image/avif,image/webp,image/apng,*/*;q=0.8,"
             "application/signed-exchange;v=b3;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/111.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url=url, headers=KEY)
    return response


def get_games(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all(
        'div', class_="partnereventshared_SaleSectionContainer_1UD2h "
                      "partnersaledisplay_SaleSectionContainer_2IK75 "
                      "center_row_trgt ItemCount_1"
    )
    games = []
    for page in pages:
        game = {
            "photo": page.find('div', class_="salepreviewwidgets_CapsuleImage_cODQh"),
            "price": page.find('div', class_="salepreviewwidgets_StoreSalePriceBox_Wh0L8"),
            "link": page.find('div', class_="salepreviewwidgets_CapsuleImage_cODQh").find('a').get('href'),
        }
        games.append(game)
    return games