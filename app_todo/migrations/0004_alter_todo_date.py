# Generated by Django 3.2.9 on 2022-04-20 17:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0003_auto_20220420_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 20, 17, 47, 51, 996778, tzinfo=utc), verbose_name='Когда выполнить'),
        ),
    ]