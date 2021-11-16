import requests
from bs4 import BeautifulSoup


def parser_time_wait(city, transport, number_transport, station):
    # парсит время ожидания транспорта: прошлое, будущее, следующее - будущее
    # waiting time for transport soars: past, future, next - future
    url = f'https://kogda.by/routes/{city}/{transport}/{number_transport}/{station}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    take_for_was_and_now = soup.find_all('div', {"class": "content-block-desktop"})
    take_for_will_be = soup.find_all('span', {"class": "future"})
    for q in take_for_was_and_now:
        soup2 = BeautifulSoup(str(q), 'lxml')
        was = soup2.find('span', {"class": "passed"})
        now = soup2.find('span', {"class": "future"})
    for q in take_for_will_be:
        soup2 = BeautifulSoup(str(q), 'lxml')
        will_be = soup2.find('span')
        all_time = [' '.join(was.split()), ' '.join(now.text.split()), ' '.join(will_be.text.split())]

    return all_time


# parser_time_wait('minsk', 'autobus', '24', 'Воронянского%20-%20ДС%20Зелёный%20Луг-6/Жуковского')


def parser_station(city, transport, number_transport):
    # парсит начальные и конечные остановку транспорта
    # steam initial and final stops of transport
    url = f'https://kogda.by/routes/{city}/{transport}/{number_transport}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    first_way = soup.find_all('div', {"id": "direction-0-heading"})
    second_way = soup.find_all('div', {"id": "direction-1-heading"})

    for q in first_way:
        soup2 = BeautifulSoup(str(q), 'lxml')
        first = soup2.find('a').contents[0]
    for q in second_way:
        soup2 = BeautifulSoup(str(q), 'lxml')
        second = soup2.find('a').contents[0]
    return f"{' '.join(first.text.split())} \n {' '.join(second.text.split())}"


# parser_station('minsk','autobus','69')


def parser_all_station(city, transport, number_transport):
    # парсит все остановки в две стороны транспорта
    # steaming all stops in two directions of transport
    url = f'https://kogda.by/routes/{city}/{transport}/{number_transport}'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    firs_all_station = soup.find('ul', {"class": "list-group"}).text
    second_all_station = soup.find('div', {"id": "direction-1"}).text
    return f"{' '.join(firs_all_station.split())} \n \n{' '.join(second_all_station.split())}"
# parser_all_station('minsk','autobus','69')
