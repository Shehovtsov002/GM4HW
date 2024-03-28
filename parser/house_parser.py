import requests
from bs4 import BeautifulSoup

MAIN_URL = "https://www.house.kg/snyat"
BASE_URL = "https://www.house.kg"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response.text


def get_houses():
    html = get_html(MAIN_URL)
    soup = BeautifulSoup(html, 'html.parser')
    houses_links = [a['href'] for a in soup.select('.left-side a')]
    houses_titles = [a.get_text().strip() for a in soup.select('.left-side a')]
    houses_adresses = [adr.get_text().strip() for adr in soup.select('.address')]

    list_houses = []
    for title, link, adress in zip(houses_titles, houses_links, houses_adresses):
        list_houses.append({
            'title': title,
            'address': adress,
            'link': BASE_URL + link
        })

    return list_houses


if __name__ == '__main__':
    print(get_houses())
