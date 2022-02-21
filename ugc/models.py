from django.db import models


# Create your models here.

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя в соц сети',
        unique=True,
    )

    def __str__(self):
        return f'@{self.external_id}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class SelectedTransport(models.Model):
    profile = models.ForeignKey(
        to='Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    transport_type = models.TextField(
        verbose_name='Избранный транспорт'
    )
    transport_number = models.TextField(
        verbose_name='Избранный транспорт'
    )

    def __str__(self):
        return f'{self.transport_type} {self.transport_number}'

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'


class SelectedStation(models.Model):
    profile = models.ForeignKey(
        to='Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    transport_type = models.TextField(
        verbose_name='Избранный транспорт'
    )
    transport_number = models.TextField(
        verbose_name='Избранный транспорт'
    )
    station = models.TextField(
        verbose_name='Избранный маршрут'
    )

    def __str__(self):
        return f'{self.station}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
