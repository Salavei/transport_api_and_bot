import requests
from bs4 import BeautifulSoup
import re

USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Accept-Language': 'ru',
}

dict = {
    'автобус': 'autobus',
    'autobus': 'autobus',
    'автик': 'autobus',
    'овтобус': 'autobus',
    'АВТОБУС': 'autobus',
    'Autobus': 'autobus',
    'Автик': 'autobus',
    'Автобус': 'autobus',
    'Трамвай': 'tram',
    'трам': 'tram',
    'tram': 'tram',
    'тромвай': 'tram',
    'трамвай': 'tram',
    'Трам': 'tram',
    'ТРАМВАЙ': 'tram',
    'Tram': 'tram',
    'Тромвай': 'tram',
    'Троллейбус': 'trolleybus',
    'тралеуйбус': 'trolleybus',
    'тралик': 'trolleybus',
    'trolleybus': 'trolleybus',
    'троллейбус': 'trolleybus',
    'Тралеуйбус': 'trolleybus',
    'Тралик': 'trolleybus',
    'Trolleybus': 'trolleybus',
}


def parser_time_wait(name_left, name_right, give_first_way, give_second_way, station):
    if give_first_way:
        soup = BeautifulSoup(requests.get(give_first_way, headers=USER_AGENT).text, 'lxml')
        if 'рейсов нет' not in soup.find('div', {'class': 'info-message'}).text.strip():
            take_for_was_and_now = soup.find_all('span', {"class": "future"})[0].text.strip()
            take_for_will_be = soup.find_all('span', {"class": "future"})[1].text.strip()
            all_time = take_for_was_and_now, take_for_will_be
        else:
            all_time = '❗ Сегодня у маршрута рейсов нет ❗'
    else:
        all_time = ' ❗️Такой остановки в этом направлении не существует❗️'
    if give_second_way:
        soup_two = BeautifulSoup(requests.get(give_second_way, headers=USER_AGENT).text, 'lxml')
        if 'рейсов нет' not in soup_two.find('div', {'class': 'info-message'}).text.strip():
            take_for_was_and_now_two = soup_two.find_all('span', {"class": "future"})[0].text.strip()
            take_for_will_be_two = soup_two.find_all('span', {"class": "future"})[1].text.strip()
            all_time_two = take_for_was_and_now_two, take_for_will_be_two
        else:
            all_time_two = '❗ Сегодня у маршрута рейсов нет ❗'
    else:
        all_time_two = ' ❗️Такой остановки в этом направлении не существует❗️'
    return f"{name_left}, {all_time}", f"{name_right}, {all_time_two}"


def parser_station_n(transport, number_transport, station):
    if dict.get(transport):
        r = requests.get(f'https://kogda.by/routes/minsk/{dict.get(transport)}/{number_transport}',
                         headers=USER_AGENT)
        soup = BeautifulSoup(r.text, 'lxml')
        name_left = soup.find('div', {"id": "direction-0-heading"}).find('a').text.strip()
        name_right = soup.find('div', {"id": "direction-1-heading"}).find('a').text.strip()
        first_way = soup.find('div', {"id": "direction-0"}).find(
            'ul', {"class": "list-group"}).find("a", text=re.compile(station[0].upper() + station[1:].lower()))
        second_way = soup.find('div', {"id": "direction-1"}).find(
            'ul', {"class": "list-group"}).find("a", string=re.compile(station[0].upper() + station[1:].lower()))
        if first_way:
            give_first_way = first_way.get('href')
        else:
            give_first_way = None
        if second_way:
            give_second_way = second_way.get('href')
        else:
            give_second_way = None
        return parser_time_wait(name_left, name_right, give_first_way, give_second_way, station)
    return 'Неверное название транспорта (Автобус, Трамвай, Троллейбус) ❌'


def parser_all_station(transport, number_transport):
    """
        Если нет правильной инфы , то пишет None
    """
    if dict.get(transport):
        r = requests.get(f'https://kogda.by/routes/minsk/{dict.get(transport)}/{number_transport}',
                         headers=USER_AGENT)
        soup = BeautifulSoup(r.text, 'lxml')
        if soup.find('ul', {"class": "list-group"}):
            firs_all_station = soup.find('ul', {"class": "list-group"}).text
            second_all_station = soup.find('div', {"id": "direction-1"}).text
            return ' '.join(firs_all_station.split()), ' '.join(second_all_station.split())
    return 'Неверное название транспорта (Автобус, Трамвай, Троллейбус) ❌'
