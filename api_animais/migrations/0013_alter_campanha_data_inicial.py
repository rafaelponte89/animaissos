# Generated by Django 4.1.1 on 2022-10-28 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_animais', '0012_alter_campanha_data_inicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campanha',
            name='data_inicial',
            field=models.DateField(default=datetime.date(2022, 10, 28)),
        ),
    ]
