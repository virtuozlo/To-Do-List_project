# Generated by Django 3.2.9 on 2022-04-22 11:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0007_auto_20220422_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 22, 11, 52, 40, 895503, tzinfo=utc), verbose_name='Когда выполнить'),
        ),
    ]
