# Generated by Django 4.1.1 on 2022-10-13 21:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_animais', '0009_alter_campanha_animal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campanha',
            old_name='finalidade',
            new_name='informacoes',
        ),
        migrations.AlterField(
            model_name='campanha',
            name='data_inicial',
            field=models.DateField(default=datetime.date(2022, 10, 13)),
        ),
        migrations.AlterField(
            model_name='portoseguro',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
