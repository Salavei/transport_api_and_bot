import requests
from bs4 import BeautifulSoup
import re


def parser_time_wait(hah, hah_two, left, right, station):
    if hah == None:
        all_time = ' ❗️Такой отановки в этом направлении не существует❗️'
    else:
        r = requests.get(hah, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        })
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        take_for_was_and_now = soup.find_all('div', {"class": "content-block-desktop"})
        take_for_will_be = soup.find_all('span', {"class": "future"})
        for q in take_for_was_and_now:
            soup2 = BeautifulSoup(str(q), 'lxml')
            now = soup2.find('span', {"class": "future"})
        for q in take_for_will_be:
            soup2 = BeautifulSoup(str(q), 'lxml')
            will_be = soup2.find('span')
            all_time = [' '.join(now.text.split()), ' '.join(will_be.text.split())]
    if hah_two == None:
        all_time_two = ' ❗️Такой отановки в этом направлении не существует❗️'
    else:
        r_two = requests.get(hah_two, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        })
        html_two = r_two.text
        soup_two = BeautifulSoup(html_two, 'lxml')
        take_for_was_and_now_two = soup_two.find_all('div', {"class": "content-block-desktop"})
        take_for_will_be_two = soup_two.find_all('span', {"class": "future"})
        for q in take_for_was_and_now_two:
            soup2 = BeautifulSoup(str(q), 'lxml')
            now = soup2.find('span', {"class": "future"})
        for q in take_for_will_be_two:
            soup2 = BeautifulSoup(str(q), 'lxml')
            will_be = soup2.find('span')
            all_time_two = [' '.join(now.text.split()), ' '.join(will_be.text.split())]
    return f"⬅️{' '.join(left.text.split())}\n🕐{all_time} \n", f"\n➡️{' '.join(right.text.split())}\n🕐{all_time_two}"


def parser_station(transport):
    bus = ['автобус', 'АВТОБУС', 'autobus', 'автик', 'овтобус']
    trum = ['Трамвай', 'трам', 'ТРАМВАЙ', 'tram', 'тромвай']
    trami = ['Троллейбус', 'тралеуйбус', 'тралик', 'trolleybus', 'троллейбус']
    metr = ['метро', 'МЕТРО', 'Метро', 'metro']
    if transport in bus:
        transport = 'autobus'
    elif transport in trami:
        transport = 'trolleybus'
    elif transport in trum:
        transport = 'tram'
    elif transport in metr:
        transport = 'metro'
    else:
        print('транспорта не существует')
    return transport


def parser_station_n(transport, number_transport, station):
    transport = parser_station(transport)
    station = station

    url = f'https://kogda.by/routes/minsk/{transport}/{number_transport}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    left = soup.find_all('div', {"id": "direction-0-heading"})
    right = soup.find_all('div', {"id": "direction-1-heading"})

    for q in left:
        soup2 = BeautifulSoup(str(q), 'lxml')
        send_left_station = soup2.find('a').contents[0]
    for q in right:
        soup2 = BeautifulSoup(str(q), 'lxml')
        second_right_station = soup2.find('a').contents[0]

    first_way = soup.find_all('div', {"id": "direction-0"})
    second_way = soup.find_all('div', {"id": "direction-1"})

    for q in first_way:
        first_second_way = q.find_all('ul', {"class": "list-group"})
        for q in first_second_way:
            if q.find("a", string=re.compile(station)) == None:
                cc = None
            else:
                hah = q.find("a", string=re.compile(station)).get('href')
                cc = hah
    for q in second_way:
        second_second_way = q.find_all('ul', {"class": "list-group"})
        for q in second_second_way:
            if q.find("a", string=re.compile(station)) == None:
                hah_two = None
            else:
                hah_two = q.find("a", string=re.compile(station)).get('href')
        return parser_time_wait(cc, hah_two, send_left_station, second_right_station, station)


def parser_all_station(transport, number_transport):
    transport = parser_station(transport)
    url = f'https://kogda.by/routes/minsk/{transport}/{number_transport}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    firs_all_station = soup.find('ul', {"class": "list-group"}).text
    second_all_station = soup.find('div', {"id": "direction-1"}).text
    return f"⬅️ {' '.join(firs_all_station.split())} \n \n➡️ {' '.join(second_all_station.split())}"
