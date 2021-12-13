from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from ugc.models import Message
from ugc.models import Profile
from ugc.models import SelectedTransport
from ugc.models import SelectedStation
from .parser import parser_all_station, parser_station_n

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

client_status_station = {}
client_status_transport = {}


def log_errors(f):
    """ Функция для отлова ошибок """

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_send_log(update: Update, context: CallbackContext):
    """Функция вывода всех остановок избранного транспорта, с проверкой на их существование """
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    read_file_log = os.path.join('app.log')
    with open(read_file_log, 'r') as file:
        context.bot.send_document(chat_id=815021893, document=file,
                                  filename='tg_error_log.txt')


@log_errors
def do_allstation(update: Update, context: CallbackContext):
    """Функция вывода всех остановок избранного транспорта, с проверкой на их существование """
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() == 0:
        update.message.reply_text(
            text='❌ Вы еще не добавили ни одного транспорта ❌'
        )
    elif SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() == 1:
        take_data_transport = SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True)
        transport_one = [x for x in str(take_data_transport[0]).split()]
        give_transport_in_func_one = parser_all_station(transport_one[0], transport_one[1])
        update.message.reply_text(
            text=f'✨ Все остановки🚏 {transport_one[0].upper()} 🚍: {transport_one[1]}\n {give_transport_in_func_one}',
        )
    else:
        take_data_transport = SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True)
        transport_one = [x for x in str(take_data_transport[0]).split()]
        transport_two = [x for x in str(take_data_transport[1]).split()]
        give_transport_in_func_one = parser_all_station(transport_one[0], transport_one[1])
        give_transport_in_func_two = parser_all_station(transport_two[0], transport_two[1])

        update.message.reply_text(
            text=f'✨ Все остановки🚏 {transport_one[0].upper()} 🚍: {transport_one[1]}\n {give_transport_in_func_one}',
        )
        update.message.reply_text(
            text=f'✨ Все остановки🚏 {transport_two[0].upper()} 🚍: {transport_two[1]} \n {give_transport_in_func_two}',
        )


@log_errors
def do_live_station(update: Update, context: CallbackContext):
    """ Функция вывода времени ожидания избранных остановок в 2-ух направлениях """
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 0:
        update.message.reply_text(
            text='❌ Вы еще не добавили остановку ❌'
        )
    elif SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 1:
        take_data_station = SelectedStation.objects.filter(profile=p).values_list('station', flat=True)
        station_one = [x for x in str(take_data_station[0]).split()]
        give_station_in_func_one = parser_station_n(station_one[0], station_one[1],
                                                    station_one[2][0].upper() + station_one[2][1:])
        # # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод
        update.message.reply_text(
            text=f'✨ {station_one[0].upper()} 🚍 {station_one[1]}\n✨ Остановка 🚏: {station_one[2][0].upper() + station_one[2][1:]}'
                 f'\n{f"{give_station_in_func_one[0]}{give_station_in_func_one[1]}"}\n\n🚯Оставляйте, пожалуйста, талоны другим людям♥️')
    else:
        take_data_station = SelectedStation.objects.filter(profile=p).values_list('station', flat=True)
        station_one = [x for x in str(take_data_station[0]).split()]
        station_two = [x for x in str(take_data_station[1]).split()]
        give_station_in_func_one = parser_station_n(station_one[0], station_one[1],
                                                    station_one[2][0].upper() + station_one[2][1:])
        give_station_in_func_two = parser_station_n(station_two[0], station_two[1],
                                                    station_two[2][0].upper() + station_two[2][1:])
        # # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод
        update.message.reply_text(
            text=f'✨ {station_one[0].upper()} 🚍 {station_one[1]}\n✨ Остановка 🚏: {station_one[2][0].upper() + station_one[2][1:]}'
                 f'\n{f"{give_station_in_func_one[0]}{give_station_in_func_one[1]}"}\n')
        update.message.reply_text(
            text=f'✨ {station_two[0].upper()} 🚍 {station_two[1]}\n✨ Остановка 🚏: {station_two[2][0].upper() + station_two[2][1:]}'
                 f'\n{f"{give_station_in_func_two[0]}{give_station_in_func_two[1]}"}\n\n🚯Оставляйте, пожалуйста, талоны другим людям♥️',
        )


@log_errors
def do_add_station(update: Update, context: CallbackContext):
    """ Записывает в словарь значение о том, что пользователь собрался добавить остановку """
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() >= 2:
        update.message.reply_text(
            text=f'❌ Нельзя добавить больше 2-ух остановок ❌'
        )
    else:
        client_status_station[chat_id] = 'wait_for_data_station'
        update.message.reply_text(
            text=f'🛠Добавить избранную остановку(Автобус 100 Козлова)\n☝️ВАЖНО: если остановка начинается что-то вроде'
                 f' Площадь / Станция и т.д, \n❗️писать нужно само название - Немига, Якуба, Победы❗:'
        )


@log_errors
def do_add_transport(update: Update, context: CallbackContext):
    """ Записывает в словарь значение о том, что пользователь собрался добавить транспорт """
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() >= 2:
        update.message.reply_text(
            text=f'❌ Нельзя добавить больше 2-ух транспорта❌'
        )
    else:
        client_status_transport[chat_id] = 'wait_for_data_transport'
        update.message.reply_text(
            text=f'🛠Добавить избранный транспорт(Автобус 100):'
        )
    # not correctly work, need add (add text after the command)
    # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод


@log_errors
def do_dell_transport(update: Update, context: CallbackContext):
    """ Функция удаляет !!Пока что!! весь транспорт из БД человека"""
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() == 0:
        update.message.reply_text(
            text=f'❌ У Вас нет транспорта ❌'
        )
    elif SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() == 1:
        update.message.reply_text(
            text=f'🛠{SelectedTransport.objects.filter(profile=p)[0]}: ⚠️ удален'
        )
        SelectedTransport.objects.filter(profile=p)[0].delete()

    else:
        update.message.reply_text(
            text=f'🛠{SelectedTransport.objects.filter(profile=p)[1]}: ⚠️ удален'
        )
        SelectedTransport.objects.filter(profile=p)[1].delete()


@log_errors
def do_dell_station(update: Update, context: CallbackContext):
    """ Функция удаляет !!Пока что!! все остановки из БД человека"""
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 0:
        update.message.reply_text(
            text=f'❌ У Вас нет остановок ❌'
        )
    elif SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 1:
        update.message.reply_text(
            text=f'🛠Остановка 🚏 {SelectedStation.objects.filter(profile=p)[0]}: ⚠️ удалена'
        )
        SelectedStation.objects.filter(profile=p)[0].delete()

    else:
        update.message.reply_text(
            text=f'🛠Остановка 🚏 {SelectedStation.objects.filter(profile=p)[1]}: ⚠️ удалена'
        )
        SelectedStation.objects.filter(profile=p)[1].delete()


@log_errors
def do_echo_add(update: Update, context: CallbackContext):
    """ Функция которая реагирует на сообщения, но если в словаре есть значения на запис, то будет сохранять в БД инфу
    Если человек собрался добавить Остановку , то в словаре будет  -  wait_for_data_station и после ввода добавит остановку
    Если человек собрался добавить Транспорт , то в словаре будет  -  wait_for_data_transport и после ввода добавит транспорт
    Просто если ввел 2 слова, то среагирует показ всех остановок, а если 3 , то время ожидания транспорта с отсановки
    """
    try:
        chat_id = update.message.chat_id
        text = update.message.text
        if text[0].isdigit() == False:
            # _ - булевый флаг, кот означает профиль создан только что или нет! p - объект профиля, кот взят из базы
            p, _ = Profile.objects.get_or_create(
                external_id=chat_id,
                defaults={
                    'name': update.message.from_user.username,
                }
            )
            station_one = [x for x in text.split()]
            check_station_to_save = parser_station_n(station_one[0], station_one[1],
                                                     station_one[2][0].upper() + station_one[2][1:])
            if chat_id in client_status_station and client_status_station[
                chat_id] == 'wait_for_data_station' and SelectedStation.objects.filter(profile=p).values_list('station',
                                                                                                              flat=True).count() < 2 and \
                    check_station_to_save[0].find("❗️") != -1 and check_station_to_save[1].find("❗️") != -1:
                del client_status_station[chat_id]
                update.message.reply_text(
                    text=f'❗ Маршрут не сохранен. Проверьте корректность названия остановки ❗'
                )
            elif chat_id in client_status_station and client_status_station[
                chat_id] == 'wait_for_data_station' and SelectedStation.objects.filter(profile=p).values_list('station',
                                                                                                              flat=True).count() < 2:
                add_data_station = SelectedStation.objects.create(profile=p, station=text)
                add_data_station.save
                del client_status_station[chat_id]
                update.message.reply_text(
                    text=f'✨ Маршрут от остановки 🚏: {station_one[2]} добавлен ✅'
                )
            # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод
            elif chat_id in client_status_transport and client_status_transport[
                chat_id] == 'wait_for_data_transport' and SelectedTransport.objects.filter(profile=p).values_list(
                'transport',
                flat=True).count() < 2:
                add_data_transport = SelectedTransport.objects.create(profile=p, transport=text)
                add_data_transport.save
                del client_status_transport[chat_id]
                # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод
                update.message.reply_text(
                    text=f'✨ Транспорт 🚍: {add_data_transport} добавлен ✅'
                )

            else:
                hand_add_st = [x for x in text.split(' ')]
                if len(hand_add_st) == 2:
                    # hand_trans_data = parser_station(hand_add_st[0], hand_add_st[1])
                    # update.message.reply_text(
                    #     text=f'✨ Направления {hand_add_st[1]} {hand_add_st[0].upper()} 🚍 : \n{hand_trans_data}',
                    # )
                    hand_trans_data = parser_all_station(hand_add_st[0], hand_add_st[1])
                    update.message.reply_text(
                        text=f'✨ Все остановки🚏 {hand_add_st[0].upper()} 🚍: {hand_add_st[1]}\n {hand_trans_data}',
                    )
                else:
                    hand_trans_data = parser_station_n(hand_add_st[0], hand_add_st[1],
                                                       hand_add_st[2][0].upper() + hand_add_st[2][1:])
                    update.message.reply_text(
                        text=f'✨ {hand_add_st[0].upper()} 🚍 {hand_add_st[1]}\n✨ Остановка 🚏: \n{hand_add_st[2][0].upper()}'
                             f'{hand_add_st[2][1:]}\n{f"{hand_trans_data[0]} {hand_trans_data[1]}"}\n'
                             f'\n🚯Оставляйте, пожалуйста, талоны другим людям♥️'
                    )
            Message(
                profile=p,
                text=text,
            ).save()
        else:
            update.message.reply_text(
                text=f'❌ Нужно начинать с транспорта!!( Автобус 100 Московская ) или ( Автобус 100 ) ❌\n'
            )
    except IndexError:
        update.message.reply_text(
            text=f'❌ Я Вас не понимаю. Введите /help чтобы узнать как я работаю ❌',
        )


@log_errors
def do_help(update: Update, context: CallbackContext):
    """ Выводит информацию по боту"""
    chat_id = update.message.chat_id
    text = update.message.text
    # _ - булевый флаг, кот означает профиль создан только что или нет! p - объект профиля, кот взят из базы
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    update.message.reply_text(
        text=
        f'\nЕсли введешь:'

        f'\n➡️ вид интересующего тебя транспорта и его номер - откроется полный список остановок на его маршруте'
        f'\n➡️ Пример: Автобус 100'
        f'\n➡️ вид транспорта, его номер и название остановки - увидишь время отправления транспорта'
        f'\n➡️ ☝️ВАЖНО: если остановка начинается что-то вроде Площадь / Станция и т.д, ❗️писать нужно само название - Немига, Якуба, Победы❗️️'
        f'\n➡️ Пример: Автобус 100 Козлова'
        f'\n➡️ /tadd - добавишь далее введённый транспорт в избранные (не более 2-х)'
        f'\n➡️ /sadd - добавишь далее введённую остановку в избранные (не более 2-х)'
        f'\n➡️ /all - получишь все остановки избранного транспорта'
        f'\n➡️ /live - узнаешь время отправления избранного транспорта с избранной остановки'
        f'\n➡️ /tdell - удалишь избранный транспорт'
        f'\n➡️ /sdell - удалишь избранную остановку'
        f'\nУдачи и в путь!😊'
    )
    Message(
        profile=p,
        text=text,
    ).save()


@log_errors
def do_start(update: Update, context: CallbackContext):
    """ Стартует бота """
    chat_id = update.message.chat_id
    text = update.message.text
    # _ - булевый флаг, кот означает профиль создан только что или нет! p - объект профиля, кот взят из базы
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    update.message.reply_text(
        text=f'Привет! Давай я помогу тебе поскорее добраться до точки назначения🔜 /help', reply_markup=markup
    )
    Message(
        profile=p,
        text=text,
    ).save()


reply_keyboard = [['/tadd', '/sadd'],
                  ['/all', '/live'],
                  ['/tdell', '/sdell']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


class Command(BaseCommand):
    help = 'Телеграм-Бот'

    def handle(self, *args, **options):
        """ Подключение бота"""
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
            con_pool_size=8,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            # base_url=settings.PROXY_URL,
        )
        print(bot.get_me())
        # 2 -- обработчики
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        message_handler2 = CommandHandler('all', do_allstation)
        updater.dispatcher.add_handler(message_handler2)

        message_handler4 = CommandHandler('live', do_live_station)
        updater.dispatcher.add_handler(message_handler4)

        message_handler4 = CommandHandler('tadd', do_add_transport)
        updater.dispatcher.add_handler(message_handler4)

        message_handler5 = CommandHandler('sadd', do_add_station)
        updater.dispatcher.add_handler(message_handler5)

        message_handler6 = CommandHandler('help', do_help)
        updater.dispatcher.add_handler(message_handler6)

        message_handler7 = CommandHandler('start', do_start)
        updater.dispatcher.add_handler(message_handler7)

        message_handler8 = CommandHandler('tdell', do_dell_transport)
        updater.dispatcher.add_handler(message_handler8)

        message_handler9 = CommandHandler('sdell', do_dell_station)
        updater.dispatcher.add_handler(message_handler9)

        message_handler9 = CommandHandler('log', do_send_log)
        updater.dispatcher.add_handler(message_handler9)

        message_handler = MessageHandler(Filters.text, do_echo_add)
        updater.dispatcher.add_handler(message_handler)

        # 3 -- обработчик
        updater.start_polling()
        updater.idle()
