from django.db import models


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
        blank=False,
        verbose_name='Название транспорта'
    )
    transport_number = models.TextField(
        blank=False,
        verbose_name='Номер транспорта'
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
        blank=False,
        verbose_name='Название транспорта'
    )
    transport_number = models.TextField(
        blank=False,
        verbose_name='Номер транспорта'
    )
    station = models.TextField(
        blank=False,
        verbose_name='Остановка'
    )

    def __str__(self):
        return f'{self.station}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
