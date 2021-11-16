import requests
from bs4 import BeautifulSoup


def parser_time_wait(city, transport, number_transport, station):
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
        #добавить поиск 3-тьего столбика
    return all_time
parser_time_wait('minsk', 'autobus', '24', 'Воронянского%20-%20ДС%20Зелёный%20Луг-6/Жуковского')



def parser_station(city, transport, number_transport):
    url = f'https://kogda.by/routes/{city}/{transport}/{number_transport}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    quote_boxes = soup.find_all('div', {"id": "direction-0-heading"})
    quote_boxes1 = soup.find_all('div', {"id": "direction-1-heading"})

    for q in quote_boxes:
        soup2 = BeautifulSoup(str(q), 'lxml')
        left = soup2.find('a').contents[0]
    for q in quote_boxes1:
        soup2 = BeautifulSoup(str(q), 'lxml')
        right = soup2.find('a').contents[0]
        # print(' '.join(left.text.split()), ' '.join(right.text.split()), sep='\n')
        wwww =[' '.join(left.text.split()),' '.join(right.text.split())]
    return wwww

# parser_station('minsk','autobus','69')


# def parser_all_station(city, transport, number_transport):
#     url = f'https://kogda.by/routes/{city}/{transport}/{number_transport}'
#     r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#     html = r.text
#     soup = BeautifulSoup(html, 'lxml')
#     quote_boxes = soup.find('ul', {"class": "list-group"}).text
#     quote_boxes1 = soup.find('div', {"id": "direction-1"}).text
#
#     return print(','.join(quote_boxes.split()),','.join(quote_boxes1.split()), sep='\n \n')
#
# parser_all_station('minsk','autobus','69')


