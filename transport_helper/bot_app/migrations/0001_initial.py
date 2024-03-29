# Generated by Django 4.0.3 on 2023-01-13 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.PositiveBigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.TextField(verbose_name='name_of_transport')),
                ('transport_number', models.TextField(verbose_name='number_of_transport')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot_app.profile', verbose_name='profile')),
            ],
        ),
        migrations.CreateModel(
            name='SelectedStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.TextField(verbose_name='name_of_transport')),
                ('transport_number', models.TextField(verbose_name='number_of_transport')),
                ('station', models.TextField(verbose_name='station')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot_app.profile', verbose_name='Профиль')),
            ],
        ),
    ]
