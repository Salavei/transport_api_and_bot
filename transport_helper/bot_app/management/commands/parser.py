import requests
from bs4 import BeautifulSoup
import re

USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Accept-Language': 'ru',
}

dict = {
    'Bus': 'autobus',
    'bus': 'autobus',
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


def parser_time_wait(station_data):
    data_with_time_and_stop = []
    if station_data:
        for step in range(1, len(station_data), 2):
            soup = BeautifulSoup(requests.get(station_data[step], headers=USER_AGENT).text, 'lxml')
            if 'рейсов нет' not in soup.find('div', {'class': 'info-message'}).text.strip():
                take_for_was_and_now = soup.find_all('span', {"class": "future"})[0].text.strip()
                take_for_will_be = soup.find_all('span', {"class": "future"})[1].text.strip()
                data_with_time_and_stop.append([station_data[step-1], take_for_was_and_now, take_for_will_be])
            else:
                data_with_time_and_stop = 'There are no routes today'
        return data_with_time_and_stop
    return 'Incorrect name of transport (Bus, Tram, Trolleybus)'


def parser_station_n(transport, number_transport, station):
    if dict.get(transport):
        r = requests.get(f'https://kogda.by/routes/minsk/{dict.get(transport)}/{number_transport}',
                         headers=USER_AGENT)
        soup = BeautifulSoup(r.text, 'lxml')
        station_data = []
        for step in range(2):
            station_data.append(soup.find('div', {"id": f"direction-{step}-heading"}).find('a').text.strip())
            get_direction = soup.find('div', {"id": f"direction-{step}"})
            get_direction_list_group = get_direction.find('ul', {"class": "list-group"})
            station_data.append(get_direction_list_group.find("a", text=re.compile(station[0].upper() + station[1:].lower())).get('href'))
        return parser_time_wait(station_data)
    return 'Incorrect name of transport (Bus, Tram, Trolleybus)'


def parser_all_station(transport, number_transport):
    """
        If there is no correct information, it says None
    """
    if dict.get(transport):
        r = requests.get(f'https://kogda.by/routes/minsk/{dict.get(transport)}/{number_transport}',
                         headers=USER_AGENT)
        soup = BeautifulSoup(r.text, 'lxml')
        if soup.find('ul', {"class": "list-group"}):
            firs_all_station = soup.find('ul', {"class": "list-group"}).text
            second_all_station = soup.find('div', {"id": "direction-1"}).text
            return ' '.join(firs_all_station.split()), ' '.join(second_all_station.split())
    return 'Incorrect name of transport (Bus, Tram, Trolleybus)'
