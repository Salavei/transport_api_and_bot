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
from .parser import parser_time_wait


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
def do_count(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    count = Message.objects.filter(profile=p).count()

    update.message.reply_text(
        text=f'У вас {count} сообщений',
    )


@log_errors
def do_work(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    test = parser_time_wait('minsk', 'autobus', '24', 'ДС%20Зелёный%20Луг-6%20-%20Воронянского/Романовская%20Слобода')

    update.message.reply_text(
        text=f'От работы --- автобус в {test[0]}, а еще один в {test[1]}',
    )


@log_errors
def do_home(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    test = parser_time_wait('minsk', 'autobus', '24', 'Воронянского%20-%20ДС%20Зелёный%20Луг-6/Жуковского')

    update.message.reply_text(
        text=f'От дома --- автобус в {test[0]}, а еще один в {test[1]}',
    )


@log_errors
def do_test(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    dd = text
    uu = [x for x in dd.split(' ')]
    print(uu)
    # _ - булевый флаг, кот означает профиль создан только что или нет! p - объект профиля, кот взят из базы
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    test = parser_time_wait(uu[0],uu[1],uu[2],uu[3])
    update.message.reply_text(
        text=f'автобус с остановки {uu[3]}:\n в {test[0]} и {test[1]}'
    )

    Message(
        profile=p,
        text=text,
    ).save()







# @log_errors
# def do_echo(update: Update, context: CallbackContext):
#     chat_id = update.message.chat_id
#     text = update.message.text
#     # _ - булевый флаг, кот означает профиль создан только что или нет! p - объект профиля, кот взят из базы
#     p, _ = Profile.objects.get_or_create(
#         external_id=chat_id,
#         defaults={
#             'name': update.message.from_user.username,
#         }
#     )
#     Message(
#         profile=p,
#         text=text,
#     ).save()
#
#     reply_text = 'Ваш ID ={}\n\n{}'.format(chat_id, text)
#     update.message.reply_text(
#         text=reply_text,
#     )


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
        message_handler0 = CommandHandler('count', do_count)
        updater.dispatcher.add_handler(message_handler0)

        message_handler1 = CommandHandler('work', do_work)
        updater.dispatcher.add_handler(message_handler1)

        message_handler2 = CommandHandler('home', do_home)
        updater.dispatcher.add_handler(message_handler2)

        message_handler = MessageHandler(Filters.text, do_test)
        # message_handler = MessageHandler(Filters.all, do_test)
        updater.dispatcher.add_handler(message_handler)
        #
        # message_handler = MessageHandler(Filters.text, do_echo)
        # updater.dispatcher.add_handler(message_handler)

        # 3 -- обработчик
        updater.start_polling()
        updater.idle()
