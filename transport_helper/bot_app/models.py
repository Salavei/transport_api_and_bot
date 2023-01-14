from django.db import models


class Profile(models.Model):
    external_id = models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return f'@{self.external_id}'


class SelectedTransport(models.Model):
    profile = models.ForeignKey(to='Profile', verbose_name='profile', on_delete=models.PROTECT)
    transport_type = models.CharField(max_length=255, null=False, verbose_name='name_of_transport')
    transport_number = models.CharField(max_length=255, null=False, verbose_name='number_of_transport')

    def __str__(self):
        return f'{self.transport_type} {self.transport_number}'


class SelectedStation(models.Model):
    profile = models.ForeignKey(to='Profile', verbose_name='Профиль', on_delete=models.PROTECT)
    transport_type = models.CharField(max_length=255, null=False, verbose_name='name_of_transport')
    transport_number = models.CharField(max_length=255, null=False, verbose_name='number_of_transport')
    station = models.CharField(max_length=255, null=False, verbose_name='station')

    def __str__(self):
        return f'{self.station}'
