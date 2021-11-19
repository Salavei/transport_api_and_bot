from django.db import models


# Create your models here.

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя в соц сети',
        unique=True,
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
    )

    def __str__(self):
        return f'@{self.external_id} {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class SelectedTransport(models.Model):
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    transport = models.TextField(
        verbose_name='Избранный транспорт'
    )
    created_at = models.DateTimeField(
        verbose_name='Время сохранения',
        auto_now_add=True,
    )
    def __str__(self):
        return f'{list((self.transport).split())}'

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'

class SelectedStation(models.Model):
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    station = models.TextField(
        verbose_name='Избранный маршрут'
    )
    created_at = models.DateTimeField(
        verbose_name='Время сохранения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.station}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
