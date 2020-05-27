import requests
from bs4 import BeautifulSoup
import csv
import os


URL = "https://stopgame.ru/review/new"
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
FILE = '../games.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_ = 'page')
    if pagination:
        return int(pagination[-1].get_text())
    print(pagination)




def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items_1 = soup.find_all('div', class_ = 'lent-block review_rating_bg_1')
    items_2 = soup.find_all('div', class_ = 'lent-block review_rating_bg_2')
    items_3 = soup.find_all('div', class_ = 'lent-block review_rating_bg_3')
    items_4 = soup.find_all('div', class_ = 'lent-block review_rating_bg_4')
    games = []
    for item_1 in items_1:
        games.append({
            'title': item_1.find('div', class_ = 'title lent-title').get_text(strip=True),
            'link': item_1.find('div', class_='title lent-title').get('href'),
            'views': item_1.find('div', class_='lent-views').get_text(),
            'date': item_1.find('div', class_='lent-date').get_text(),
            'rating': 'Garbage'
        })
    for item_2 in items_2:
        games.append({
            'title': item_2.find('div', class_ = 'title lent-title').get_text(strip=True),
            'link': item_2.find('div', class_='title lent-title').get('href'),
            'views': item_2.find('div', class_='lent-views').get_text(),
            'date': item_2.find('div', class_='lent-date').get_text(),
            'rating': 'May be'
        })
    for item_3 in items_3:
        games.append({
            'title': item_3.find('div', class_ = 'title lent-title').get_text(strip=True),
            'link': item_3.find('div', class_='title lent-title').get('href'),
            'views': item_3.find('div', class_='lent-views').get_text(),
            'date': item_3.find('div', class_='lent-date').get_text(),
            'rating': 'Ok'
        })
    for item_4 in items_4:
        games.append({
            'title': item_4.find('div', class_ = 'title lent-title').get_text(strip=True),
            'link': item_4.find('div', class_='title lent-title').get('href'),
            'views': item_4.find('div', class_='lent-views').get_text(),
            'date': item_4.find('div', class_='lent-date').get_text(),
            'rating': 'Exelent'
        })
    return games


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Name','Link','Views','Date','Rating'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['views'], item['date'], item['rating']])


def parse():
    URL = input('Give me link: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        games = []
        pages_count = get_pages_count(html.text)
        for page in range(1,pages_count + 1):
            print(f'Parsing page {page} from {pages_count}...')
            html = get_html(URL, params = {'p':page})
            games.extend(get_content(html.text))
        save_file(games, FILE)
        print(f'Get {len(games)} games')
        os.startfile(FILE)
    else:
        print("Error")


parse()
