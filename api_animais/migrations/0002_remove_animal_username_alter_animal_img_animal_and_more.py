# Generated by Django 4.1.1 on 2022-10-02 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_animais', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='username',
        ),
        migrations.AlterField(
            model_name='animal',
            name='img_animal',
            field=models.ImageField(upload_to='fotos_animais'),
        ),
        migrations.AlterField(
            model_name='campanha',
            name='data_inicial',
            field=models.DateField(default=datetime.date(2022, 10, 2), editable=False),
        ),
    ]