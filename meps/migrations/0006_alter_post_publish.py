# Generated by Django 3.2.14 on 2022-07-12 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meps', '0005_auto_20220712_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 7, 12, 14, 45, 31, 843277, tzinfo=utc)),
        ),
    ]
