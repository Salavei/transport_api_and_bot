import requests
from bs4 import BeautifulSoup


def parser_data(city,transport,number_transport,station):
    url = f'https://kogda.by/routes/{city}/{transport}/{number_transport}/{station}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    quote_boxes = soup.find_all('div', {"class": "content-block-desktop"})

    for q in quote_boxes:
        soup2 = BeautifulSoup(str(q), 'lxml')

        was = soup2.find('span', {"class": "passed"})
        now = soup2.find('span', {"class": "future"})
        will_be = soup2.find('span', {"class": "future"})
        all_time = [' '.join(was.text.split()), ' '.join(now.text.split()), ' '.join(will_be.text.split())]
    return all_time

parser_data('minsk','autobus','24','Воронянского%20-%20ДС%20Зелёный%20Луг-6/Жуковского')
