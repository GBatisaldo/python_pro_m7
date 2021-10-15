# Generated by Django 3.2.6 on 2021-10-15 16:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoDjango',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('numero_de_modulos', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('data', models.DateTimeField(default=datetime.datetime(2021, 10, 15, 13, 27, 2, 746008), verbose_name='Publicado em')),
            ],
        ),
    ]
