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
from .parser import  parser_station, parser_all_station, parser_station_n


client_status_station = {}
client_status_transport = {}


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_allstation(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() == 0:
        update.message.reply_text(
            text='У вас нет transport'
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
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 0:
        update.message.reply_text(
            text='У вас нет station'
        )
    elif SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 1:
        take_data_station = SelectedStation.objects.filter(profile=p).values_list('station', flat=True)
        station_one = [x for x in str(take_data_station[0]).split()]
        give_station_in_func_one = parser_station_n(station_one[0], station_one[1], station_one[2])
        # # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод
        update.message.reply_text(
            text=f'✨ {station_one[0].upper()} 🚍 {station_one[1]}\n✨ Остановка 🚏: {station_one[2]}'
                 f'\n{f"{give_station_in_func_one[0]}{give_station_in_func_one[1]}"}')
    else:
        take_data_station = SelectedStation.objects.filter(profile=p).values_list('station', flat=True)
        station_one = [x for x in str(take_data_station[0]).split()]
        station_two = [x for x in str(take_data_station[1]).split()]
        give_station_in_func_one = parser_station_n(station_one[0], station_one[1], station_one[2])
        give_station_in_func_two = parser_station_n(station_two[0], station_two[1], station_two[2])
        # # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод
        update.message.reply_text(
            text=f'✨ {station_one[0].upper()} 🚍 {station_one[1]}\n✨ Остановка 🚏: {station_one[2]}'
                 f'\n{f"{give_station_in_func_one[0]}{give_station_in_func_one[1]}"}\n')
        update.message.reply_text(
            text=f'✨ {station_two[0].upper()} 🚍 {station_two[1]}\n✨ Остановка 🚏: {station_two[2]}'
                 f'\n{f"{give_station_in_func_two[0]}{give_station_in_func_two[1]}"}',
        )


@log_errors
def do_add_station(update: Update, context: CallbackContext):
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
            text=f'🛠Добавить избранную остановку:'
        )


@log_errors
def do_add_transport(update: Update, context: CallbackContext):
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
            text=f'🛠Добавить избранный транспорт:'
        )
    # not correctly work, need add (add text after the command)
    # обратиться к БД и достать инфу транспорта, запихнуть в функцию и показать вывод


@log_errors
def do_dell_transport(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedTransport.objects.filter(profile=p).values_list('transport', flat=True).count() == 0:
        update.message.reply_text(
            text=f'❌ У Вас нет транспорта❌'
        )
    else:
        tran = SelectedTransport.objects.filter(profile=p).delete()
        update.message.reply_text(
            text=f'🛠{tran} удален'
        )


@log_errors
def do_dell_station(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    if SelectedStation.objects.filter(profile=p).values_list('station', flat=True).count() == 0:
        update.message.reply_text(
            text=f'❌ У Вас нет остановок❌'
        )
    else:
        tran = SelectedStation.objects.filter(profile=p).delete()
        update.message.reply_text(
            text=f'🛠{tran} удален'
        )


@log_errors
def do_echo_add(update: Update, context: CallbackContext):
    try:
        chat_id = update.message.chat_id
        text = update.message.text
        # _ - булевый флаг, кот означает профиль создан только что или нет! p - объект профиля, кот взят из базы
        p, _ = Profile.objects.get_or_create(
            external_id=chat_id,
            defaults={
                'name': update.message.from_user.username,
            }
        )
        if chat_id in client_status_station and client_status_station[
            chat_id] == 'wait_for_data_station' and SelectedStation.objects.filter(profile=p).values_list('station',
                                                                                                          flat=True).count() < 2:
            add_data_station = SelectedStation.objects.create(profile=p, station=text)
            add_data_station.save
            del client_status_station[chat_id]
            station_one = [x for x in text.split()]
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
                hand_trans_data = parser_station_n(hand_add_st[0], hand_add_st[1], hand_add_st[2])
                update.message.reply_text(
                    text=f'✨ {hand_add_st[0].upper()} 🚍 {hand_add_st[1]}\n✨ Остановка 🚏: \n{hand_add_st[2]}\n{f"{hand_trans_data[0]} {hand_trans_data[1]}"}\n'
                )
        Message(
            profile=p,
            text=text,
        ).save()
    except IndexError:
        update.message.reply_text(
            text=f'❌ Неверый ввод ❌',
        )


@log_errors
def do_help(update: Update, context: CallbackContext):
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
        f'\n/all - показать все остановки избранного транспорта'
        f'\n/live - показать время отправления с избранного транспорта'
        f'\n/sadd - добавить остановку в избранные(не более 2-ух)'
        f'\n/tadd - добавить транспорт в избранные(не более 2-ух)'
        f'\n/tdell - удалить весь транспорт'
        f'\n/sdell - удалить все остановки'
        f'\nЧтобы узнать направления автобуса, введи название транспорта и номер'
        f'\nПример: автобус 69'
        f'\nЧтобы узнать время до автобуса, введи название транспорта, номер и остановку'
        f'\nПример: автобус 69 2-е кольцо',
    )
    Message(
        profile=p,
        text=text,
    ).save()


@log_errors
def do_start(update: Update, context: CallbackContext):
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
        text=f'Привет, для начала предлагаю тебе ознакомиться с командами бота\n /help',
    )
    Message(
        profile=p,
        text=text,
    ).save()


class Command(BaseCommand):
    help = 'Телеграм-Бот'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
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

        message_handler = MessageHandler(Filters.text, do_echo_add)
        updater.dispatcher.add_handler(message_handler)

        # 3 -- обработчик
        updater.start_polling()
        updater.idle()
